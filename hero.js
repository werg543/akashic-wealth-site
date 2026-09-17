const FINAL="assets/hero-final.png",FIELD="assets/hero-field.png",MAP="assets/hero-map.png",MAP2="assets/hero-map2.png";
const BASE=1.425,GAPS=[1.22,1.5,1.5],D=[BASE,BASE*GAPS[0],BASE*GAPS[0]*GAPS[1],BASE*GAPS[0]*GAPS[1]*GAPS[2]],T_END=D[3]*1.05,EXIT_SPAN=0.85,POW=3.0,AMP=1100,SPLIT=0.968;
const cv=document.getElementById('hero-canvas'),gl=cv.getContext('webgl2',{antialias:false,alpha:false});
const vs=`#version 300 es
in vec2 a;out vec2 v;void main(){v=a*.5+.5;v.y=1.-v.y;gl_Position=vec4(a,0,1);}`;
const fs=`#version 300 es
precision highp float;in vec2 v;out vec4 o;
uniform sampler2D uFinal,uField,uMap,uMap2;uniform vec2 uScale,uOff;uniform vec4 uE;uniform float uSplit,uEx;
float sideOf(vec2 p){return (p.x+p.y)<uSplit?0.:1.;}
int idOf(vec2 p){return int(floor(texture(uMap,p).r*255./50.+.5));}
float toneOf(vec2 p){return (texture(uMap,p).g*255.-128.)/255.;}
bool inside(vec2 p){return all(greaterThanEqual(p,vec2(0.)))&&all(lessThanEqual(p,vec2(1.)));}
void main(){
  vec2 uv=(v-.5)*uScale+.5;
  float side=sideOf(uv);vec2 dir=side>.5?-uOff:uOff;
  float e[4];e[0]=uE.x;e[1]=uE.y;e[2]=uE.z;e[3]=uE.w;
  vec3 col=texture(uField,uv).rgb;bool hit=false;
  for(int k=0;k<4;k++){
    vec2 p=uv+dir*(1.-e[k]);
    if(inside(p)&&sideOf(p)==side&&idOf(p)==k){
      col=texture(uField,p).rgb+toneOf(p)+(texture(uFinal,p).rgb-texture(uField,p).rgb);hit=true;break;}
  }
  if(!hit&&idOf(uv)==4)col+=(texture(uFinal,uv).rgb-texture(uField,uv).rgb)*smoothstep(.88,1.,e[3]);
  if(uEx>0.){vec3 m2=texture(uMap2,uv).rgb;float p=m2.r;float pr=1.-uEx*1.08;float rv=smoothstep(p-.02,p+.004,pr);col=mix(texture(uField,uv).rgb,col,rv);col+=vec3(.95,.80,.42)*exp(-pow((p-pr)/.012,2.))*m2.b*.7*(1.-smoothstep(.9,1.,uEx));}
  o=vec4(col,1.);
}`;
function sh(t,s){const x=gl.createShader(t);gl.shaderSource(x,s);gl.compileShader(x);if(!gl.getShaderParameter(x,gl.COMPILE_STATUS))throw gl.getShaderInfoLog(x);return x;}
const pg=gl.createProgram();gl.attachShader(pg,sh(gl.VERTEX_SHADER,vs));gl.attachShader(pg,sh(gl.FRAGMENT_SHADER,fs));gl.linkProgram(pg);gl.useProgram(pg);
const buf=gl.createBuffer();gl.bindBuffer(gl.ARRAY_BUFFER,buf);gl.bufferData(gl.ARRAY_BUFFER,new Float32Array([-1,-1,3,-1,-1,3]),gl.STATIC_DRAW);
const loc=gl.getAttribLocation(pg,'a');gl.enableVertexAttribArray(loc);gl.vertexAttribPointer(loc,2,gl.FLOAT,false,0,0);
const U=n=>gl.getUniformLocation(pg,n);
function tex(img,unit,nearest){const t=gl.createTexture();gl.activeTexture(gl.TEXTURE0+unit);gl.bindTexture(gl.TEXTURE_2D,t);gl.texImage2D(gl.TEXTURE_2D,0,gl.RGB,gl.RGB,gl.UNSIGNED_BYTE,img);const f=nearest?gl.NEAREST:gl.LINEAR;gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MIN_FILTER,f);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_MAG_FILTER,f);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_S,gl.CLAMP_TO_EDGE);gl.texParameteri(gl.TEXTURE_2D,gl.TEXTURE_WRAP_T,gl.CLAMP_TO_EDGE);return t;}
const load=src=>new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=src;});
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const ease=t=>{t=Math.min(1,Math.max(0,t));return 1-Math.pow(1-t,POW);};
let t0=performance.now(),IW=1690,IH=931;
function resize(){const dpr=Math.min(2,devicePixelRatio||1);cv.width=cv.clientWidth*dpr;cv.height=cv.clientHeight*dpr;gl.viewport(0,0,cv.width,cv.height);
  const ca=cv.width/cv.height,ia=IW/IH;gl.uniform2f(U('uScale'),ca>ia?1:ca/ia,ca>ia?ia/ca:1);}
Promise.all([load(FINAL),load(FIELD),load(MAP),load(MAP2)]).then(([a,b,c,d])=>{IW=a.width;IH=a.height;tex(a,0,false);tex(b,1,false);tex(c,2,true);tex(d,3,false);
  const L=Math.hypot(IW,IH),dx=IW/L,dy=IH/L;
  gl.uniform1i(U('uFinal'),0);gl.uniform1i(U('uField'),1);gl.uniform1i(U('uMap'),2);gl.uniform1i(U('uMap2'),3);gl.uniform1f(U('uSplit'),SPLIT);
  gl.uniform2f(U('uOff'),dx*AMP/IW,dy*AMP/IH);
  addEventListener('resize',resize);resize();t0=performance.now();
  (function f(now){const ex=Math.min(1,Math.max(0,(window.scrollY||0)/(innerHeight*EXIT_SPAN)));const t=Math.min((now-t0)/1000,T_END);gl.uniform1f(U('uEx'),ex);const E=[0,1,2,3].map(k=>reduce?1:ease(t/D[k]));gl.uniform4f(U('uE'),E[0],E[1],E[2],E[3]);gl.drawArrays(gl.TRIANGLES,0,3);requestAnimationFrame(f);})(performance.now());});
