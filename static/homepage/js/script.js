const canvas = document.getElementById("canvas");
const heroContainer = document.getElementById("hero");
const ctx = canvas.getContext("2d");
var width = canvas.width = window.innerWidth;
var height = canvas.height = window.innerHeight;
ctx.fillStyle="#FFFFFF";
ctx.lineWidth = 0.2;

class Particle{
  constructor(){
    this.x = Math.random() * width;
    this.y = Math.random() * height;
    this.size = Math.random() * 5 + 1;
    this.xA = Math.random() * 2 - 1;
    this.yA = Math.random() * 2 - 1;
    // this.angleX = Math.random() * 6.2;
    // this.angleY = Math.random() * 6.2;
    // this.vAngleX = Math.random() * 0.1 + 0.01;
    // this.vAngleY = Math.random() * 0.1 + 0.01;
  }
  update(){
    this.x+=this.xA;
    this.y+=this.yA;
    // this.x+=this.xA + Math.sin(this.angleX);
    // this.y+=this.yA + Math.cos(this.angleY);
    // this.angleX+=this.vAngleX;
    // this.angleY+=this.vAngleY;

    // this.x = this.x>width ?0:this.x;
    // this.x = this.x<0     ?width:this.x;
    // this.y = this.y>height?0:this.y;
    // this.y = this.y<0     ?height:this.y;

    if(this.x < 0|| this.x > width)this.xA*=-1;
    if(this.y < 0|| this.y > width)this.yA*=-1;
  }
  draw(alpha){
    ctx.beginPath()
    ctx.fillStyle = `rgba(255,255,255,${ alpha/mouseradius*-1 + 1 })`;
    ctx.arc(this.x,this.y,this.size,0,Math.PI * 2);
    ctx.fill();
  }
}
window.addEventListener("load",() => {
  init();
  animate();
});
const mouse={
  x:undefined,
  y:undefined
}
const mouseradius = 120;
heroContainer.addEventListener("mousemove",(e) => {
  // console.log(e);
  mouse.x = e.x;
  mouse.y = e.y;
});
// heroContainer.addEventListener("mouseover",()=>{
//   init();
//   animate();
// });
heroContainer.addEventListener("resize",()=>{
  particals=[];
  if(currentAnimationFrame != undefined){
    console.log(currentAnimationFrame);
    cancelAnimationFrame(currentAnimationFrame);
  }
  width = canvas.width = window.innerWidth;
  height = canvas.height = window.innerHeight;
  console.log(canvas.width,canvas.height);
  init();
  animate();
});


var particals = [];
function init() {
  for(let i=0;i<250;i++){
    particals.push(new Particle());
  }
}

function resetCanvas(){
  ctx.beginPath();
  ctx.fillStyle="rgba(0,0,0,1)";
  ctx.fillRect(0,0,width,height);

}
function animate(){
  ctx.clearRect(0,0,width,height);
  // resetCanvas();
  for(let i=0;i<particals.length;i++){
    const particle = particals[i];
    particle.update();
    const dx = mouse.x - particle.x,dy = mouse.y - particle.y,distance = Math.sqrt(dx*dx + dy*dy);
    if(distance < mouseradius){
      for(let j=0;j<particals.length;j++){
        if(particals[j] != particle){
          const ddx = particals[j].x - particle.x,ddy = particals[j].y - particle.y,ddistance = Math.sqrt(ddx*ddx + ddy*ddy);
          if(ddistance < mouseradius){
            ctx.beginPath();
            ctx.strokeStyle = `rgba(255,255,255,${distance/mouseradius* -1 + 1})`;
            ctx.moveTo(particle.x,particle.y);
            ctx.lineTo(particals[j].x,particals[j].y);
            ctx.stroke();
          }
        }
      }
      particals[i].draw(distance);
    }
  }
  window.currentAnimationFrame = window.requestAnimationFrame(animate);
}