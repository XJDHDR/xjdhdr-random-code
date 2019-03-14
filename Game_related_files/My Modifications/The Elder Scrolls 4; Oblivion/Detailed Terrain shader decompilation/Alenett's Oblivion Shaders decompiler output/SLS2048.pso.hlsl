//
// Generated by Microsoft (R) D3DX9 Shader Compiler 9.08.299.0000
//
// Parameters:
//
//   float4 AmbientColor;
//   sampler2D BaseMap;
//   sampler2D NormalMap;
//   float4 PSLightColor[4];
//   sampler2D ShadowMap;
//   sampler2D ShadowMaskMap;
//
//
// Registers:
//
//   Name          Reg   Size
//   ------------- ----- ----
//   AmbientColor  const_1       1
//   PSLightColor[0]  const_2        1
//   BaseMap       texture_0       1
//   NormalMap     texture_1       1
//   ShadowMap     texture_2       1
//   ShadowMaskMap texture_3       1
//

    const int4 const_0 = {2, -1, 1, 0};
    float2 texcoord_0 : TEXCOORD0;
    float2 texcoord_1 : TEXCOORD1;
    float3 texcoord_2 : TEXCOORD2_centroid;
    float3 texcoord_3 : TEXCOORD3_centroid;
    float4 texcoord_4 : TEXCOORD4;
    sampler2D texture_0;
    sampler2D texture_1;
    sampler2D texture_2;
    sampler2D texture_3;
    r0.xyzw = tex2D(texture_1, IN.texcoord_1.xy);
    r0.xyz = (2 * r0.xyz) - 1;
    r1.xyz = normalize(r0.xyz);
    r0.xyz = (IN.texcoord_3.xyz * 2) - 1;
    r0.x = saturate(dot(r0.xyz, r1.xyz));
    r0.xyz = r0.x * const_2.xyz;
    r1.x = IN.texcoord_4.z;
    r1.y = IN.texcoord_4.w;
    r1.xyzw = tex2D(texture_3, r1.xy);
    r2.xyzw = tex2D(texture_2, IN.texcoord_4.xy);
    r3.xyzw = tex2D(texture_0, IN.texcoord_0.xy);
    r0.w = r2.x - 1;
    r0.w = (r1.x * r0.w) + 1;
    r0.xyz = (r0.w * r0.xyz) + const_1.xyz;
    r0.xyz = r3.xyz * r0.xyz;
    r0.xyz = r0.xyz * IN.texcoord_2.xyz;
    r0.w = 1;
    OUT.color_0.rgba = r0.xyzw;

// approximately 20 instruction slots used (4 texture, 16 arithmetic)