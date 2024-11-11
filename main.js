// document.addEventListener('DOMContentLoaded', function() {
//     // Model options based on brand selection
//     const modelOptions = {
//         toyota: ['Camry', 'Corolla', 'RAV4'],
//         honda: ['Civic', 'Accord', 'CR-V'],
//         ford: ['F-150', 'Mustang', 'Explorer']
//     };
    
//     // Generate year options
//     const yearSelect = document.getElementById('year');
//     const currentYear = new Date().getFullYear();
//     for (let year = currentYear; year >= currentYear - 20; year--) {
//         const option = document.createElement('option');
//         option.value = year;
//         option.textContent = year;
//         yearSelect.appendChild(option);
//     }
    
//     // Update model options when brand changes
//     const brandSelect = document.getElementById('brand');
//     const modelSelect = document.getElementById('model');
    
//     brandSelect.addEventListener('change', function() {
//         modelSelect.innerHTML = '<option value="">Select Model</option>';
        
//         if (this.value) {
//             modelOptions[this.value].forEach(model => {
//                 const option = document.createElement('option');
//                 option.value = model.toLowerCase();
//                 option.textContent = model;
//                 modelSelect.appendChild(option);
//             });
//         }
//     });
    
//     // Search button functionality
//     const searchBtn = document.querySelector('.search-btn');
//     searchBtn.addEventListener('click', function() {
//         const brand = brandSelect.value;
//         const model = modelSelect.value;
//         const year = yearSelect.value;
        
//         if (brand && model && year) {
//             alert(`Searching for ${year} ${brand} ${model}`);
//             // Add your search functionality here
//         } else {
//             alert('Please select all fields');
//         }
//     });
// });


document.addEventListener('DOMContentLoaded', function () {
    // Search button functionality
    const searchBtn = document.querySelector('.search-btn');
    searchBtn.addEventListener('click', function () {
        const brand = document.getElementById('brand').value.trim();
        const model = document.getElementById('model').value.trim();
        const year = document.getElementById('year').value.trim();

        if (brand && model && year) {
            alert(`Searching for ${year} ${brand} ${model}`);
            // Add your search functionality here
        } else {
            alert('Please fill out all fields before searching.');
        }
    });
});
