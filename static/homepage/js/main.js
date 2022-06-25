const canvas = document.getElementById("canvas");
let width = canvas.width = window.innerWidth;
let height = canvas.height = window.innerHeight;
const ctx = canvas.getContext("2d");
ctx.lineWidth=1;
ctx.strokeStyle="#FFFFFF";
// ctx.fillStyle="#FFFFFF";

const mouse = {
    x:null,
    y:null
}




class Partical{
    constructor(){
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.r = Math.random() * 3 + 2;
        this.accX=Math.random() * 1 - .5;
        this.accY=Math.random() * 1 - .5;
        this.xInv = 1;
        this.yInv = 1;
        this.opacity = 0;
        this.distance = 0;
    }
    update(){
        this.x += this.accX * this.xInv;
        this.y += this.accY * this.yInv;
        const dx = mouse.x - this.x,dy = mouse.y - this.y;
        this.distance = Math.sqrt(dx*dx+dy*dy); 
        this.opacity = 1 - this.distance / 150;
        this.xInv = this.x > (width-1)?-1:this.xInv;
        this.xInv = this.x < 1? -1:this.xInv;

        this.yInv = this.y > (height-1)?-1:this.yInv;
        this.yInv = this.y < 1? -1:this.yInv;

        this.draw();
    }
    draw(){
        ctx.beginPath();
        ctx.fillStyle="rgba(255,255,255,"+this.opacity+")";
        ctx.arc(this.x,this.y,this.r,0,Math.PI * 2,false);
        ctx.fill();
    }
}

let particalArray;
let particalCount = 200;
function init(){
    particalArray = [];
    particalCount = (width > 800)?200:100;
    console.log(particalCount);
    for(var i=0;i<particalCount;i++){
        particalArray.push(new Partical());
    }
}
function connect(){
    for(let i=0;i<particalArray.length-1;i++)
        for(let j=i+1;j<particalArray.length;j++){
            if(particalArray[i].opacity > 0 && particalArray[j].opacity > 0){
                const dx = particalArray[i].x - particalArray[j].x;
                const dy = particalArray[i].y - particalArray[j].y;
                const dis = Math.sqrt(dx*dx + dy*dy);
                if(dis < 100){
                    ctx.beginPath();
                    ctx.strokeStyle = "rgba(255,255,255,"+particalArray[i].opacity+")";
                    ctx.moveTo(particalArray[i].x,particalArray[i].y);
                    ctx.lineTo(particalArray[j].x,particalArray[j].y);
                    ctx.stroke()
                }
            }
        }
}
function animation(){
    ctx.clearRect(0,0,width,height);
    for(let i=0;i<particalArray.length;i++)
        particalArray[i].update();
    connect();
    requestAnimationFrame(animation);
}
window.addEventListener("load",function(){
    init();
    animation();
});
window.addEventListener("resize",function(){
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    init();
    animation();
});
canvas.addEventListener("mousemove",function(event){
    mouse.x = event.offsetX;
    mouse.y = event.offsetY;
});