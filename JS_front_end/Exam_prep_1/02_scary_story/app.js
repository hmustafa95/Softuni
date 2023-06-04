window.addEventListener("load", solve);

function solve() {
  const firstName = document.getElementById('first-name');
  const lastName = document.getElementById('last-name');
  const age = document.getElementById('age');
  const storyTitle = document.getElementById('story-title');
  const genre = document.getElementById('genre');
  const storyContent = document.getElementById('story');
  const publishBtn = document.getElementById('form-btn');
  const previewList = document.getElementById('preview-list');
  publishBtn.addEventListener("click", publishHandler);

  function publishHandler(event) {
    event.preventDefault();
    const validInput = [firstName, lastName, age, storyTitle, storyContent].every(field => field.value.length > 0);
    if (!validInput) { return };

    const li = createHTMLElement('li', previewList, null, ['story-info']);
    const article = createHTMLElement('article', li);
    createHTMLElement('h4', article, `Name: ${firstName.value} ${lastName.value}`);
    createHTMLElement('p', article, `Age: ${age.value}`);
    createHTMLElement('p', article, `Title: ${storyTitle.value}`);
    createHTMLElement('p', article, `Genre: ${genre.value}`);
    createHTMLElement('p', article, `${storyContent.value}`);

    const saveBtn = createHTMLElement('button', li, 'Save Story', ['save-btn']);
    const editBtn = createHTMLElement('button', li, 'Edit Story', ['edit-btn']);
    const deleteBtn = createHTMLElement('button', li, 'Delete Story', ['delete-btn']);

    document.querySelector('form').reset();
    publishBtn.disabled = true;

    saveBtn.addEventListener('click', saveStory);
    editBtn.addEventListener('click', editStory);
    deleteBtn.addEventListener('click', deleteStory);
  }

  function editStory() {
    const names = document.querySelector('.story-info > article > h4').textContent.split(' ');
    firstName.value = names[1];
    lastName.value = names[2];
    const ages = document.querySelector('.story-info > article > p').textContent.split(' ');
    age.value = ages[1];
    const remaining = Array.from(document.querySelectorAll('.story-info > article > p'));
    const titles = remaining[1].textContent.split(' ');
    storyTitle.value = titles[1];
    const genres = remaining[2].textContent.split(' ');
    genre.value = genres[1];
    storyContent.value = remaining[3].textContent.trim();
    publishBtn.disabled = false;
    this.parentNode.remove();
  }

  function saveStory() {
    const mainDiv = document.getElementById('main');
    mainDiv.innerHTML = "";
    createHTMLElement('h1', mainDiv, "Your scary story is saved!");
  }
  
  function deleteStory() {
    this.parentNode.remove();
    publishBtn.disabled = false;
  }


  function createHTMLElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
    const htmlElement = document.createElement(type);

    if (content && useInnerHtml) {
        htmlElement.innerHTML = content;
    } else {
        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }

        if (content && type === 'input') {
            htmlElement.value = content;
        }
    }

    if (classes && classes.length > 0) {
        htmlElement.classList.add(...classes);
    }

    if (id) {
        htmlElement.id = id;
    }

    // { src: 'link', href: 'http' }
    if (attributes) {
        for (const key in attributes) {
            htmlElement.setAttribute(key, attributes[key])
        }
    }

    if (parentNode) {
        parentNode.appendChild(htmlElement);
    }

    return htmlElement;
  }
}
