const input = document.createElement('input');
input.type = 'file';
input.multiple = true;
input.webkitdirectory = true;
input.style.display = 'none';
document.body.appendChild(input);

input.addEventListener('change', function (e) {
    const files = e.target.files;

    for (let i = 0; i < files.length; i++) {
        if (files[i].type === 'image/jpeg' || files[i].type === 'image/png') {
            const reader = new FileReader();
            reader.readAsDataURL(files[i]);
            reader.onload = function () {
                const div = document.createElement('div');
                const a = document.createElement('a');
                const img = document.createElement('img');

                a.className = 'col-sm';
                a.setAttribute('data-lightbox', 'Additional courses');
                a.setAttribute('href', reader.result);
                img.setAttribute('src', reader.result);
                img.setAttribute('alt', files[i].name);
                a.appendChild(img);
                a.innerHTML += `<br>${files[i].name}`;
                div.appendChild(a);
                document.body.appendChild(div);
            };
        }
    }
});

input.click();
    