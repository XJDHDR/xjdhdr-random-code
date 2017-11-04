// This is a greasemonkey script, for use with the Firefox extension Greasemonkey.
// More info: http://greasemonkey.mozdev.org/
//
// ==UserScript==
// @name			Super Next Page +
// @author			Godeye & XJDHDR
// @version			0.2.4.002
// @date			2015-08-08
// @namespace		godeye
// @description 	Based on Next Page & Prefetch Next Page & AutoPagerizer
// @identifier     	https://github.com/XJDHDR/xjdhdr-random-code/raw/master/Javascripts-for-Greasemonkey-or-similar/Super_Next_Page_+.user.js
// @include          http://*
// @include          https://*
// @exclude			 http://www.baidu.com/*
// @exclude		   	 http://mail.163.com/*
// 
// 	This is a list of websites that I have found don't play nice with SNP's pre-fetching.
// @exclude			*://arstechnica.com/civis/*
// @exclude     	*://bashguru.com/*
// @exclude			*://blocklistpro.com/*
// @exclude			*://excellular.co.za/*
// @exclude			*://forum.ea.com/*
// @exclude			*://forum.spore.com/*
// @exclude			*://gamedipper.com/*
// @exclude			*://n4bb.com/*
// @exclude			*://portableapps.com/*
// @exclude			*://torrentz.eu/*
// @exclude			*://tvtropes.org/*
// @exclude			*://wayback.archive.org/web/*
// @exclude     	*://*.bashguru.com/*
// @exclude			*://*.geekzone.co.nz/*
// @exclude			*://*.google.co.za/*
// @exclude			*://*.gumtree.co.za/*
// @exclude			*://*.neiland.net/*
// @exclude			*://*.unix.com/*
// @exclude			*://*.urbandictionary.com/*
// Original script by Godeye can be found here: http://userscripts-mirror.org/scripts/show/38066
// ==/UserScript==

/*
*************************************************
>>>>>>>>>>>?????<<<<<<<<<<<<<
??:godeye
Userscript:http://userscripts.org/scripts/show/38066
Mailto:ntdrv_1@126.com

??:
????/??:
StatusInTitle 	????????????
coloredlink		????????
iconenable		?????????
historyenable	??????????
????????,???????false????
*************************************************
*/

(function() {
	if (window != top) if(checkInIframe()) return; // ????????????,?????????????
		
	
//==================================================================
	//????
	var URL = 'http://userscripts.org/scripts/show/38066';
	var VERSION = '0.2.4';
	var leftpages = 1.5;	// ???????? leftpages ????????,????????
	var scrollpos = 0.5;	// ???????? scrollpos ???????,????????
	var StatusInTitle = false; // ????????????
	var coloredlink = true;  //????????
	var iconenable = (window == top);	//?????????
	var historyenable = (window.location.hash == '');  //??????????,?????,?????ajax?????
	var historymax = 10; //??????
	var intervaltime = 50;  //???????????,??
	
//==================================================================


	
	//???????
	var COLOR = {  
	    on: '#0f0',
	    off: '#ccc',
		loading:'#ff0',
	    textdone: '#0ff',
		done: '#00f',
		not_found: '#0a0',
	    error: '#f0f'
	}
	// ??????? 
	var TEXT = (navigator.language == "zh-CN") ? {  //for chinese 
		prefetching:'????...',
		textdone:'?????...',
		textdonetip:'?????????,???????...',
		done:'?????',
		donetip:'?????????',
		error:'????:',
		errortip:'???????'
		} : {	// for other language
		prefetching:'Prefetching...',
		textdone:'Text Prefetched...',
		textdonetip:'Text Prefetched...,Now Prefetching Image...',
		done:'Prefetching Complete',
		donetip:'This page has been Prefetched',
		error:'Eorror Occurred:',
		errortip:'Can not Prefetching'
		}
		
/*
******************************************
 ??????
 *****************************************
 */
	var IconHelper = function() {
	    this.state = GM_getValue('STATE');
	    var self = this

	    var toggle = function() {self.stateToggle()}
	    this.toggle = toggle

		this.initIcon()
		this.initHelp()
	    this.icon.addEventListener("mouseover",function(){self.viewHelp()}, true)
	}

	IconHelper.prototype.initHelp = function() {
	    var helpDiv = document.createElement('div')
	    helpDiv.setAttribute('id', 'nextpage_help')
	    helpDiv.setAttribute('style', 'padding:5px;position:fixed;' +
	                     'top:-200px;right:3px;font-size:10px;' +
	                     'background:#fff;color:#000;border:1px solid #ccc;' +
	                     'z-index:256;text-align:left;font-weight:normal;' +
	                     'line-height:120%;font-family:verdana;')

	    var toggleDiv = document.createElement('div')
	    toggleDiv.setAttribute('style', 'margin:0 0 0 50px;text-align:right;')
	    var a = document.createElement('a')
	    a.setAttribute('class', 'nextpage_link')
	    a.innerHTML = 'on/off'
	    a.href = 'javascript:void(0)'
	    var self = this
	    var toggle = function() {
	        self.stateToggle()
	        helpDiv.style.top = '-200px'
	    }
	    a.addEventListener('click', toggle, false)
	    toggleDiv.appendChild(a)

	    var s = '<div style="width:100px; float:left;">'
	    for (var i in COLOR) {
	        s += '<div style="float:left;width:1em;height:1em;' +
	            'margin:0 3px;background-color:' + COLOR[i] + ';' +
	            '"></div><div style="margin:0 3px">' + i + '</div>'
	    }
	    s += '</div>'
	    var colorDiv = document.createElement('div')
	    colorDiv.innerHTML = s
		helpDiv.appendChild(toggleDiv)
	    helpDiv.appendChild(colorDiv)
	    

	    var versionDiv = document.createElement('div')
	    versionDiv.setAttribute('style', 'clear:both;')
	    versionDiv.innerHTML = '<a href="' + URL +
	        '">Super Next Page</a> ' + VERSION
	    helpDiv.appendChild(versionDiv)
	    document.body.appendChild(helpDiv)

	    var proc = function(e) {
	        var c_style = document.defaultView.getComputedStyle(helpDiv, '')
	        var s = ['top', 'left', 'height', 'width'].map(function(i) {
	            return parseInt(c_style.getPropertyValue(i)) })
	        if (e.clientX < s[1] || e.clientX > (s[1] + s[3] + 11) ||
	            e.clientY < s[0] || e.clientY > (s[0] + s[2] + 11)) {
	                helpDiv.style.top = '-200px'
	        }
	    }
	    helpDiv.addEventListener('mouseout', proc, false)
	    this.helpLayer = helpDiv
	}

	IconHelper.prototype.viewHelp = function() {
	    this.helpLayer.style.top = '3px'
	}



	IconHelper.prototype.stateToggle = function() {
	    if (this.state == 'enable') {
	        this.disable()
	    }
	    else {
	        this.enable()
	    }
	}

	IconHelper.prototype.enable = function() {
	    this.state = 'enable'
		GM_setValue('STATE','enable');
	    this.icon.style.background = COLOR['on']
	    this.icon.style.opacity = 1
	}

	IconHelper.prototype.disable = function() {
	    this.state = 'disable'
		GM_setValue('STATE','disable');
	    this.icon.style.background = COLOR['off']
	    this.icon.style.opacity = 0.5
	}








	IconHelper.prototype.initIcon = function() {
	    var div = document.createElement("div")
	    div.setAttribute('id', 'nextpage_icon')
	    with (div.style) {
	        fontSize   = '12px'
	        position   = 'fixed'
	        top        = '3px'
	        right      = '3px'
	        background = COLOR['on']
	        color      = '#fff'
	        width = '10px'
	        height = '10px'
	        zIndex = '255'
	        if (this.state != 'enable') {
	            background = COLOR['off']
	        }
	    }
	    document.body.appendChild(div)
	    this.icon = div
	}


	IconHelper.prototype.error = function() {
	    this.icon.style.background = COLOR['error']
	}

	IconHelper.prototype.set = function(s) {
	    if (this.state == 'enable') {
			this.icon.style.background = COLOR[s]
		}
	}
	
	IconHelper.prototype.remove = function() {
		var s = document.getElementsByTagId('nextpage_help');
		if (s) s.parentNode.removeChild(s); 
		var t = document.getElementsByTagId('nextpage_icon');
		if (t) t.parentNode.removeChild(t); 
	}
	
	
	ap = (iconenable) ? (new IconHelper()):'';
	


/*
******************************************
???????
 *****************************************
 */	
 
	//???????	
	var readyfornext = false;  //??????????
	var prefetched = false;  //?????
	var currenturl = location.href;  //?????URL,????????,????????????,
    var checked = false;  //???????
    var delay = false;	//????
    var next = {}; //?????
	var nextlinks;
	var newhistory = true;  //?????????
	var lasthistory = new  Object;  //????????
	var lasthistorypushed = false;  //???????????
	

    var previous = {};
    // ?????????
    next.texts      = [ 'next',
                        'next page',
                        'old',
                        'older',
                        'earlier',
                        '??',
                        '??',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '??',
                        '??',
                        '??',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???'
                      ];
    // ?????????
    previous.texts  = [ 'previous',
                        'prev',
                        'previous page',
                        'new',
                        'newer',
                        'later',
                        '??',
                        '??',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '??',
                        '??',
                        '??',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???',
                        '???'
                      ];
    // ?????????
    next.miswords   = { "???": 30,
                        "???": 30,
                        "???": 30,
                        "???": 30,
                        "???": 30,
                        ">>": 2000,
                        "»": 2000
                      }
    previous.miswords = { "???": 30,
                          "???": 30,
                          "???": 30,
                          "???": 30,
                          "???": 30,
                          "<<": 2000,
                          "«": 2000
                        }

    // ????????
    getCustom(next, "next");
    getCustom(previous, "previous");
    // ??????
    registerMenu("next");
    registerMenu("previous");
    
    // ???????????????
    next.texts.push(">>");
    next.texts.push(">");
    next.texts.push("»");
    next.texts.push("›");
    previous.texts.push("<<");
    previous.texts.push("<");
    previous.texts.push("«");
    previous.texts.push("‹");

    // ?????????????????(?????)
    var preRegexp  = '(^\\s*(?:[<‹«]*|[>›»]*|[\\(\\[??[?]?)\\s*)';
    var nextRegexp = '(\\s*(?:[>›»]*|[\\)\\]??]?]?)\\s*$)';

    // ???????????
    function getCustom(aObj, key) {
      var site, re;
      var cKeyWords = GM_getValue("custom_" + key, "");
      var words = cKeyWords.split(/,|,/);
      for each (var w in words) {
        site = null;
        if (/^\s*{\s*(\S*?)\s*}(.*)$/.test(w)) {
          site = RegExp.$1;
          w = RegExp.$2;
          site = site.replace(/[\/\?\.\(\)\+\-\[\]\$]/g, "\\$&").replace(/\*/g, "\.*");
        }
        w = w.replace(/\\/g, "\\").replace(/^\s+|\s+$/g, "");
        if (w) {
          if (site) {
            re = eval('/' + site + '/i');
            if (re.test(currenturl))
              aObj.texts.push(w);
          }
          else
            aObj.texts.push(w);
        }
      }
    }

    // ????
    function registerMenu(key) {
      if (navigator.language == "zh-CN") {
        var word = key == "next" ? "???" : "???";
        GM_registerMenuCommand("Next Page " + word + "???", function(){setCustom(key, word)});
      }
      else {
        GM_registerMenuCommand("Next Page custom_" + key, function(){setCustom(key, key)});
      }
    }

    // ???????
    function setCustom(k, w) {
      var text = navigator.language == "zh-CN" ? "???“"+w+"”????,?“,”?????" : "Please enter the "+w+" page key-words, split with ','.";
      var result = prompt(text, GM_getValue("custom_" + k, ""));
      if (result != null) GM_setValue("custom_" + k, result);
    }

    function checkLinks() {
      var link, text, ldnc, lnc, ldpc, lpc, num, digChked, digStart, linkNumber, found;
      var regexp = new RegExp();
      // ???????
      var links = document.getElementsByTagName('A');
      for (var i = 0; i < links.length; i++) {
        link = links[i];

        // ?????????
        if (!link.offsetParent || link.offsetWidth == 0 || link.offsetHeight == 0 || !link.hasAttribute("href") && !link.hasAttribute("onclick"))
          continue;
        // ????
        if (/(?:^|\s)(?:monthlink|weekday|day|day[\-_]\S+)(?:\s|$)/i.test(link.className))
          continue;
		
		//?????id?calss?rel??
		//ADD: 0.2.4 ????rel?????
        if (/^nextlink/i.test(link.id) || /^linknext/i.test(link.id) ||
            /(^|\s)nextlink/i.test(link.className) || /(^|\s)linknext/i.test(link.className) || link.rel.toLowerCase() == 'next')
          next.link = link;
        if (/^prev(ious)?link/i.test(link.id) || /^linkprev(ious)?/i.test(link.id) ||
            /(^|\s)prev(ious)?link/i.test(link.className) || /(^|\s)linkprev(ious)?/i.test(link.className) || link.rel.toLowerCase() == 'prev')
          previous.link = link;

        text = link.textContent;
        if (!text) {
          // ????????,??????alt?????????title
		  //BUGFIX: 0.2.4 childNodes???????!
		  //for each (var img in link.childNodes) {
          for (var j = 0; j < link.childNodes; j++) {
			img = link.childNodes[j];
            if (img.localName.toUpperCase() == "IMG") {
              text = img.alt || link.title || img.title;
              if (text) break;
            }
          }
          if (!text) continue;
        }
        text = text.toLowerCase().replace(/^\s+|\s+$/g, "");
        if (!text) continue;

        // ?????
        if (isDigital(text)) {
          if (digChked) continue;
          linkNumber = parseInt(RegExp.$1);
          if (!digStart) {
          // ?????????????????
            if (isCurrentPageNumber(link, linkNumber, -1)) {
              next.link = link;
              next.found = true;
              next.pos = i;
              digStart = digChked = true;
              ldpc = i + 30;
              continue;
            }
            // ??,??????????????
            else if (isCurrentPageNumber(link, linkNumber, 0)) {
              // ???????????“???”???
              if (getNextLink(link, linkNumber+1, true)) {
                next.pos = i;
                digStart = digChked = true;
                ldpc = i + 30;
                continue;
              }
              // ???????????????
              digChked = true;
              // ?????30??????“???”?????,????????
              ldnc = i + 30;
            }
            // ???????????
            digStart = true;
          }
          // ?????????????????
          var tmpNode = isCurrentPageNumber(link, linkNumber, 1);
          if (tmpNode) {
            previous.link = link;
            previous.found = true;
            previous.pos = i;
            // ????????????“???”???
            if (getNextLink(tmpNode, linkNumber+2, true))
              break;
            // ???????????????
            digChked = true;
            // ?????30??????“???”?????,????????
            ldnc = i + 30;
          }
          continue;
        }
        else {
          found = false;
          if (!next.found && !(lnc < i) && !(ldnc < i)) {
            for (var j = 0; j < next.texts.length; j++) {
              if (regexp.compile(preRegexp + next.texts[j] + nextRegexp, 'i').test(text)) {
                // ???“???”???
                found = true;
                next.link = link;
                num = next.miswords[next.texts[j]];
                // ?“???”??????????,?????????????
                (num == null) ? next.found = true : lnc = i + num;
                break;
              }
            }
          }
          if (!next.digital && lnc < i) next.found = true;

          if (!found && !previous.found && !(lpc < i) && !(ldpc < i)) {
            for (var j = 0; j < previous.texts.length; j++) {
              if (regexp.compile(preRegexp + previous.texts[j] + nextRegexp, 'i').test(text)) {
                // ???“???”???
                previous.link = link;
                num = previous.miswords[previous.texts[j]];
                // ?“???”??????????,?????????????
                (num == null) ? previous.found = true : lpc = i + num;
                break;
              }
            }
          }
          if (lpc < i) previous.found = true;
          // ?????????????
          digChked = digStart = null;
        }

        // ??“???”?“???”???????????????????????,??????
        if (next.found && previous.found ||
            next.found && i > next.pos + 30 ||
            previous.found && i > previous.pos + 30)
          break;
      }
      // ??????????“???”?,???????????1????????,2??“???”?
      if (!next.found && !next.link && next.digital)
        next.link = next.digital;

      if (next.link) next.found = true;
      if (previous.link) previous.found = true;

      if (!next.found && !previous.found)
        checkButtons();
    }

    // ??????
    function checkButtons() {
      var but, text, found;
      var regexp = new RegExp();
      var buts = document.getElementsByTagName('INPUT');
      for (var i = 0; i < buts.length; i++) {
        but = buts[i];
        if (but.hasAttribute("disabled") || !(/^button$/i.test(but.type) && but.getAttribute("onclick"))) continue;

        text = but.value;
        found = false;
        if (!next.found) {
          for (var j = 0; j < next.texts.length; j++) {
            if (regexp.compile(preRegexp + next.texts[j] + nextRegexp, 'i').test(text)) {
              // ???“???”???
              next.link = but;
              next.found = found = true;
              break;
            }
          }
        }

        if (!found && !previous.found) {
          for (var j = 0; j < previous.texts.length; j++) {
            if (regexp.compile(preRegexp + previous.texts[j] + nextRegexp, 'i').test(text)) {
              // ???“???”???
              previous.link = but;
              previous.found = true;
              break;
            }
          }
        }
        if (next.found && previous.found) break;
      }
    }

    // ??????????,type: 1 ???;-1 ???
    function getSiblingNode(node, type) {
      if (!node) return null;
      node = getSibling(node, type);
      while (node && (node.nodeName == "#coment" ||
            (/^\s*[\]]?]?[,\|]?\s*[\[[?]?\s*$/.test(node.textContent))))
        node = getSibling(node, type);
      return node;
    }
    function getSibling(aNode, type) {
      if (!aNode) return null;
      if (isOnlyNode(aNode)) {
        try {
          aNode = (type == 1 ? aNode.parentNode.nextSibling : aNode.parentNode.previousSibling);
          if (skipNode(aNode))
            aNode = (type == 1 ? aNode.nextSibling : aNode.previousSibling);
          aNode = aNode.childNodes[0];
          if (skipNode(aNode))
            aNode = aNode.nextSibling;
        }
        catch (e) {return null;}
      }
      else {
        aNode = (type == 1 ? aNode.nextSibling : aNode.previousSibling);
      }
      return aNode;
    }
    function isOnlyNode(n) {
      return !n.nextSibling && !n.previousSibling ||
             !n.nextSibling && skipNode(n.previousSibling) && !n.previousSibling.previousSibling ||
             !n.previousSibling && skipNode(n.nextSibling) && !n.nextSibling.nextSibling ||
             skipNode(n.previousSibling) && !n.previousSibling.previousSibling &&
             skipNode(n.nextSibling) && !n.nextSibling.nextSibling;
    }
    function skipNode(sNode) {
      return sNode && /*sNode.nodeName == "#text" &&*/ (/^\s*$/.test(sNode.textContent));
    }

    // ??????????????,number:??
    function getNextLink(node, number, set) {
      var tNode = getSiblingNode(node, 1);
      if (tNode && tNode.nodeName == "A" && isDigital(tNode.textContent)) {
        if (RegExp.$1 == number) {
          // ???????
          if (set) {
            next.link = tNode;
            next.found = true;
          }
          return tNode;
        }
      }
      return null;
    }

    function isDigital(str, t) {
      str = str.replace(/^\s+|\s+$/g, "");
      if (t == -1)
        str = str.split(/\s+/).pop();
      else if (t == 1)
        str = str.split(/\s+/)[0];
      return (/^(\d+)$/.test(str)) ||
             (/^\[(\d+)\]$/.test(str)) ||
             (/^?(\d+)?$/.test(str)) ||
             (/^[(\d+)]$/.test(str)) ||
             (/^<(\d+)>$/.test(str)) ||
			 (/^(\d+),$/.test(str));	//***[????]????1,2,3,4?????
    }

    // ????????????,type:-1,0,1 ???????????????????
    function isCurrentPageNumber(node, linkNum, type) {
      var tNode = (type == 0 ? node : getSiblingNode(node, type));
      if (tNode && (tNode.nodeName != "A" && isDigital(tNode.textContent, type) ||
          tNode.nodeName == "A" && !tNode.hasAttribute("onclick") &&
          (!tNode.href && isDigital(tNode.textContent, type) || !(/\/#[^\/]+$/.test(tNode.href)) &&
          tNode.href == currenturl && isDigital(tNode.textContent, type)))) {
        var n = linkNum + type;
        if (n > 0 && RegExp.$1 == n) {
          if (next.digital) next.digital = null;
          return tNode;
        }
      }
      // ??????????,????????????,???????????????????,
      // ???????“2”??“???”????
      else if (type == 0 && !next.digital && tNode && tNode.nodeName == "A" &&
            (/^\s*[\[[?]?1[\]]?]?\s*$/.test(tNode.textContent))) {
        var two = getNextLink(tNode, 2);
        if (two && difDigital(tNode, two))
          next.digital = two;
      }
      return null;
    }

    function difDigital(node1, node2) {
      if (getStructure(node1) == getStructure(node2) && getStyleColor(node1) == getStyleColor(node2))
        return false;
      return true;
    }
    function getStructure(aNode) {
      return aNode.innerHTML.replace(/\d+/, "");
    }
    function getStyleColor(aNode) {
      return document.defaultView.getComputedStyle(aNode, null).getPropertyValue("color");
    }

    function openLink(linkNode) {
      if (!linkNode) return;
      if (linkNode.getAttribute("onclick") || (/\/#[^\/]*$/.test(linkNode.href)) &&
          linkNode.href.replace(/\/#[^\/]*$/, "") == currenturl.replace(/\/(?:#[^\/]*|#?)$/, "")) {
        // ??4D?????????????????,?????????,???????
        delay = true;
        setTimeout(cleanVars, 300);
        var e = document.createEvent("MouseEvents");
        e.initMouseEvent("click", 1, 1, window, 1, 0,0,0,0,0,0,0,0,0, linkNode);
        linkNode.dispatchEvent(e);
      }
      else if (linkNode.href && linkNode.href != currenturl){
        cleanVars();
		location.assign(linkNode.href);
      }
    }
    function cleanVars() {
      try {
		//????
		prefetched = false;
		readyfornext = false;
		nextlinks = null;
		
        checked = false;
        delay = false;
        next.link = next.found = next.digital = null;
		// next.found = next.digital = null;
        previous.link = previous.found = previous.digital = null;
        delete next.pos;
        delete previous.pos;
		if (StatusInTitle) {
			document.title = document.title.replace(/?.*?/,'');
		}
      } catch(e) {}
    }

    function onKeyDown(event) {
      // ????????????????????
      if (event.ctrlKey || event.shiftKey || event.metaKey || event.keyCode != 37 && event.keyCode != 39 || delay)
        return

      // ??????????????????
      var localName = event.target.localName.toUpperCase();
      if (localName == 'TEXTAREA' || localName == 'INPUT' || localName == 'SELECT')
        return;

      // ??????????????????,???
      if (checked && !next.found && !previous.found)
        return;

      if (!checked) {
        checkLinks();
        checked = true;
      }

      if (event.keyCode == 37 && previous.found) {
        // ????,??“???”
        openLink(previous.link)
      }
      else if (event.keyCode == 39 && next.found) {
        // ????,??“???”
		if (readyfornext) {
			
			var e = document.createEvent("MouseEvents");
			e.initMouseEvent("click", 1, 1, window, 1, 0,0,0,0,0,0,0,0,0, next.link);
			next.link.dispatchEvent(e);
		} else {
			openLink(next.link);
		}
      }
    }






	
/*
 ******************************************************************************************
 *  ???????
 ******************************************************************************************
 */
	//???????????
	function checkInIframe(){
		var r = false;
		try{
			r = parent.document.getElementById('pfnext_if').src == location;
		} catch(e){}
		return r;
	}
	
	// ?????????????top?
	function getTopest(xpresult){
		var topest=0, tmp;
		for (var i=0;i<xpresult.snapshotLength;i++){
			tmp = getTop(xpresult.snapshotItem(i));
			topest = topest > tmp?topest:tmp;
		}
		return topest;
	}

	
	//??????????????
	function getTop(e){
    var offset = e.offsetTop;
    if (e.offsetParent != null) 
        offset += getTop(e.offsetParent);
    return offset;
	}
	
	
	function onIframeLoaded(event,reg,status,statusTip,borderColor){
	    var thishref = String(event.target.location);
	    
	    
		var nexthref = String(next.link.href);
		
		if (nexthref.replace(/\/$/, '') == thishref.replace(/\/$/, '')) {
		
			if (StatusInTitle) {
				// ????????????
				document.title = document.title.replace(/?.*?/,'?' + status + '?');
			}
			
			// try {
				//????????????????????????????
				// next.link.style.border = 'solid 3px ' + borderColor;
				// next.link.title = next.link.title.replace(/?.*?/,'') + '?' + statusTip + '?';
			// } 
			// catch (e) {
			// }
			
			// ????????????????????? iframe ????????????? top ??,????????????
			
			for (var j = 0; j < nextlinks.snapshotLength; j++) {
				if(reg){	//????,??????EventListener
					nextlinks.snapshotItem(j).addEventListener('click', function(event){
						onClick(event)
					}, false)
				}
				
				if (coloredlink) {
					try {
						nextlinks.snapshotItem(j).style.border = 'solid 3px ' + borderColor;
						nextlinks.snapshotItem(j).title = nextlinks.snapshotItem(j).title.replace(/?.*?/,'') + '?' + statusTip + '?';
					} catch (e) {
					}
				}
			
			}
		}

	}
	
	
	//??????
	function onClick(event){
	    var i_html = document.getElementById('pfnext_if').contentDocument.getElementsByTagName('body')[0];
	    var html = document.getElementsByTagName('body')[0];
	    if (!html.innerHTML.length || !i_html.innerHTML.length) 
	        return;
		//?????????
		if(historyenable) {
			newhistory = true;
			var history = new Object;
			history.url = location.href;
			history.html = html.innerHTML;
			historyManage.addCase(history);
		}
		html.innerHTML = i_html.innerHTML;
		currenturl = next.link;  //????URL
		
		window.scrollTo(0, 0);
		delete ap;
		cleanVars();
		ap = (iconenable) ? (new IconHelper()):'';
	    watch_scroll();
	    event.stopPropagation();
	    event.preventDefault();
	}
	
	function matchNode(xpath, root){
    var type = XPathResult.ORDERED_NODE_SNAPSHOT_TYPE;
    var doc = root ? root.evaluate ? root : root.ownerDocument : document;
    return doc.evaluate(xpath, root || doc, null, type, null);
}
	
	var innerHeight = window.innerHeight ? window.innerHeight : document.body.clientHeight;
	function watch_scroll(){
		if (!prefetched && ap.state != 'disable') {
				if (!checked) {
					checked = true;
					checkLinks();
				}
				if (next.found && next.link.href) {
					nextlinks = matchNode('//a[@href="' + next.link.getAttribute('href') + '"]'); 
					var scrollTop = window.scrollY;
					// var scrollHeight = document.body.scrollHeight;
					var scrollHeight = getTopest(nextlinks);
					
					if (scrollHeight - innerHeight - scrollTop < innerHeight * leftpages || scrollHeight - innerHeight - scrollTop < scrollHeight * scrollpos) {
						// ?????????? leftpages * ????,????????
						prefetched = true;
						
						var prefetchContainerDiv = document.createElement('div');
	                    prefetchContainerDiv.setAttribute('style', 'position: fixed; top:0; left:0; opacity: 0;z-index: -10;');
	                    document.body.appendChild(prefetchContainerDiv);
						
						var prefetchIframe = document.createElement('iframe');
                        prefetchIframe.setAttribute('id', 'pfnext_if');
                        prefetchIframe.setAttribute('style', 'display: none;');
                        prefetchIframe.setAttribute('style', 'visibility: hidden;');
                        prefetchIframe.setAttribute('src', String(next.link.href));
                        prefetchContainerDiv.appendChild(prefetchIframe);
						
						//????????????
						if(historyenable){
							historyManage.run(historyHandle);
						}
						
						
                        if (StatusInTitle) {
                            document.title += '?' + TEXT.prefetching + '?';
                        }
						if(iconenable) ap.set('loading');
						
						var prefetchIframe = document.getElementById('pfnext_if');
                        
                        // ???????,???????,???????????
                        // ???????
                        prefetchIframe.contentWindow.addEventListener('DOMContentLoaded', function(event){
                            onIframeLoaded(event,true,TEXT.textdone,TEXT.textdonetip,COLOR.textdone);
							readyfornext = true;
							if(iconenable) ap.set('textdone');
                        }, false)
                        // ??????
                        prefetchIframe.contentWindow.addEventListener('load', function(event){
                            onIframeLoaded(event,false,TEXT.done,TEXT.donetip,COLOR.done)
							if(iconenable) ap.set('done');
                        }, false)
						// ????
                        prefetchIframe.contentWindow.addEventListener('OnError', function(event){
                             onIframeLoaded(event,false,TEXT.error+event,TEXT.errortip,COLOR.error)
							 if(iconenable) ap.set('error');
                        }, false)
						
						
						
					}
				} else {
					if(iconenable) ap.set('not_found');
				}
		}
	}

	
/*
********************************
????????
********************************
*/

var historyManage = (function(){
			var cases = new Array(historymax);  //????????
			var casesIndex = 0;	//??????
			var lastHash = 0;  //???
			var getHash = function(){ //?????
				var i, href;
				href = top.location.href;
				i = href.indexOf("#");
				return i >= 0?href.substr(i+1):0;
			};
			return {
				//???????
				addCase:function(caseData){//alert('case add!\n'+'caseIndex:'+casesIndex+'\nurl:'+caseData.url);	
					cases[casesIndex] = caseData;
					if(++casesIndex>=historymax) casesIndex = 0;
					location.hash = casesIndex
				},
				//?????????(??????)
				pushCase:function(caseData){//alert('case pushed!\n'+'caseIndex:'+casesIndex+'\nurl:'+caseData.url);
					cases[casesIndex] = caseData;
				},
				//????
				run:function(fn){
					if(getHash()!="")location.hash=getHash();
					setInterval(function(){
						var newHash = getHash();
						if(lastHash!=newHash){//alert('Hash changed!'+'\nbefore:'+lastHash+'\nafter:'+newHash);
							fn(cases[newHash]);
							lastHash = newHash;
						}
					},intervaltime);
				}
			};
		})();

	//??????	
	function historyHandle(history){
		//????????(????)
		checkLastPage();
		if(!newhistory){//alert('history changed!\nhash:'+location.hash+'\nurl:'+history.url);
			document.getElementsByTagName('body')[0].innerHTML=history.html;
			currenturl = history.url;
			window.scrollTo(0, 0);
			//????????????,????
			if (currenturl==lasthistory.url){
				delete ap;
				cleanVars();
				ap = (iconenable) ? (new IconHelper()):'';
				watch_scroll();
			}
		}
		newhistory = false;		
	}
	
	//????????(??????)
	function checkLastPage(){
		if(!newhistory&&!lasthistorypushed) {
			historyManage.pushCase(lasthistory);
			lasthistorypushed = true;
		}else if(newhistory){
			lasthistory.url = location;
			lasthistory.html = document.getElementsByTagName('body')[0].innerHTML;
			lasthistorypushed = false;
		}
	}
	
    window.addEventListener("keydown", function(e){onKeyDown(e)}, true);
	//****?????****
	window.addEventListener('load', watch_scroll, true);
	window.addEventListener('scroll', watch_scroll, true);
})();