class Body {
    constructor(scene, texturepath, radius) {
        const geometry = new THREE.SphereGeometry(radius, 32, 32);
        const texture = new THREE.TextureLoader().load(texturepath);

        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;

        const material = new THREE.MeshPhongMaterial({map:texture});

        this.sphere = new THREE.Mesh(geometry, material);
        this.scene = scene;
        this.radius = radius;
        this.orbitcolor = 0x0000ff;

        this.body_prevpos = {x: 0, y: 0, z: 0}
    }

    set_prev(x, y, z) {
        this.body_prevpos = {x: x, y: y, z: z};
    }

    change_pos(x, y, z) {
        this.sphere.position.x = x;
        this.sphere.position.y = y;
        this.sphere.position.z = z;

        this.draw_orbit();

        this.set_prev(x, y, z);
    }

    rotate() {
        this.sphere.rotation.x += 0.05;
        this.sphere.rotation.y += 0.05;
        this.sphere.rotation.z += 0.05;
    }

    set_orbitcolor(color) {
        this.orbitcolor = color;
    }

    draw_orbit() {
        const material = new THREE.LineBasicMaterial( {color: this.orbitcolor} );

        const points = [];
        points.push(new THREE.Vector3(this.body_prevpos.x, this.body_prevpos.y, this.body_prevpos.z));
        points.push(new THREE.Vector3(this.sphere.position.x, this.sphere.position.y, this.sphere.position.z));

        const geometry = new THREE.BufferGeometry().setFromPoints(points);
        const line = new THREE.Line(geometry, material);

        scene.add(line);
    }
};
