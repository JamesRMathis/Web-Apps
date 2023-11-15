let selectElement = document.getElementById('list')
selectElement.addEventListener('click', () => {
    const optionsCount = document.querySelectorAll('#list option').length

    if (optionsCount === 1) {
        let newList = prompt('What should the new list be called?')
        if (newList) {
            const option = document.createElement('option')
            option.value = newList
            option.innerHTML = newList
            selectElement.appendChild(option)
            selectElement.value = newList
        }
    }
})

selectElement.addEventListener('change', () => {
    if (selectElement.value === 'new') {
        const newList = prompt('What should the new list be called?')
        if (newList) {
            const option = document.createElement('option')
            option.value = newList
            option.innerHTML = newList
            selectElement.appendChild(option)
            selectElement.value = newList
        }
    }
})


// function getLists() {
//     fetch('/assignment7/todo/lists')
//     .then(response => response.json())
//     .then(lists => {
//         console.log(Object.keys(lists));
//         const listsDiv = document.getElementById('lists');
//         listsDiv.innerHTML = '';

//         Object.keys(lists).forEach(list => {
//             if (list === 'error') return

//             const option = document.createElement('option')
//             const selectElement = document.getElementById('list')
//             option.value = list
//             option.innerHTML = list
//             selectElement.appendChild(option)
//             selectElement.value = list

//             const listElement = document.createElement('ul');
//             listElement.innerHTML = list;
            
//             if (!Array.isArray(lists[list])) {
//                 lists[list] = [lists[list]]
//             }

//             lists[list].forEach(task => {
//                 let taskElement = document.createElement('li');
//                 taskElement.innerHTML = task.task;
//                 listElement.appendChild(taskElement);
//             });
//             listsDiv.appendChild(listElement);
//         })
//     });
// }