/**
 * скрипт создает аватарку по умолчанию (картинку) которая находится по ссылке в перенменной link_images
 * в том случаее когда пользователь не указал картинку для мура.
 * картинку можно изменить на другую поменяв лишь url в переменной var link_images
 * Проверить можно следующим образом создайте три мурра один с картинкой а другие без картинки
*/


var link_images = '<img src="https://img.icons8.com/office/250/000000/hummerstein.png">';
var murr_el_img = document.getElementsByClassName("overflow-hidden")[0];

if (!(murr_el_img.children.length)) {
    var newDiv = document.createElement("div");
    newDiv.innerHTML = link_images;
    murr_el_img.insertBefore(newDiv, murr_el_img.firstChild);
};

