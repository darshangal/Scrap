fetch('http://127.0.0.1:5000/get_ipo_data')
    .then(response => response.json())
    .then(data => {
        const nums=data.ipo_data.map((a=>{
            return {
                ...a,
                Gain: a.Gain === '-%' ? '%' : a.Gain
            }
        }))

        nums.sort((a, b) =>{ 
          
            return b.Gain.replace('%','') - a.Gain.replace('%','');}) // Sort data by 'Gain' in descending order4
       console.log(nums,data);

        const ipoDataList = document.getElementById('ipo-data-list');
        nums.forEach(ipo => {
            const listItem = document.createElement('li');
            listItem.classList.add('ipo-item');

            const nameElement = document.createElement('div');
            nameElement.classList.add('name');
            nameElement.innerHTML = `<strong>${ipo.name}</strong>`;
            listItem.appendChild(nameElement);

            // Display the rest of the data as before
            const keys = ['type', 'GMP', 'Price', 'Gain', 'Duration'];
            keys.forEach(key => {
                const keyValueElement = document.createElement('div');
                keyValueElement.innerHTML = `<strong>${key}:</strong> ${ipo[key]}`;
                listItem.appendChild(keyValueElement);
            });

            ipoDataList.appendChild(listItem);
        });
    })
    .catch(error => console.error(error));
