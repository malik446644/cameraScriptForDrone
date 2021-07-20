const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const geometry = new THREE.PlaneGeometry( 1, 1 );
const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
const cube = new THREE.Mesh( geometry, material );
scene.add(cube);

camera.position.z = 5;

// event listeners
let way = null
let speed = 0.025 * 0.3
document.addEventListener('keypress', (event) => {
    if (event.code == "KeyW") way = "farward"
    else if (event.code == "KeyS") way = "backward"
    else if (event.code == "KeyA") way = "left"
    else if (event.code == "KeyD") way = "right"
    else if (event.code == "KeyU") way = "up"
    else if (event.code == "KeyJ") way = "down"
    else if (event.code == "KeyX") way = null
});

// document.addEventListener('keyup', (event) => {
//     way = null
// });

const animate = function () {
    requestAnimationFrame( animate );

    if (way == "farward") camera.position.y += speed;
    else if (way == "backward") camera.position.y -= speed;
    else if (way == "left") camera.position.x -= speed;
    else if (way == "right") camera.position.x += speed;
    else if (way == "up") camera.position.z += speed;
    else if (way == "down") camera.position.z -= speed;

    renderer.render( scene, camera );
};

animate();