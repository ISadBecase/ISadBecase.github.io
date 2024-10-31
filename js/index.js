// 下拉三角
const dropdownIcons = document.querySelectorAll('.dropdown-icon');
dropdownIcons.forEach((icon) => {
    icon.addEventListener('click', function() {
        const dropdownContent = this.parentElement.nextElementSibling;
        const isVisible = dropdownContent.style.display === 'block';

        document.querySelectorAll('.dropdown-content').forEach(content => {
            content.style.display = 'none';
            content.previousElementSibling.querySelector('.dropdown-icon').classList.remove('rotate');
        });

        dropdownContent.style.display = isVisible ? 'none' : 'block';
        this.classList.toggle('rotate', !isVisible);
    });
});

// 内容跳转
const dropdownItems = document.querySelectorAll('.menu-item');

dropdownItems.forEach(item => {
    item.addEventListener('click', function() {
        const fileName = this.getAttribute('data-file');

        fetch(fileName)
            .then(response => response.text())
            .then(text => {
                $m.innerHTML = marked.parse(text);
            })
            .catch(error => console.error('Error fetching Markdown:', error));
    });
});
