// Un/Select all batteries
let allSelected = true;
const selectAll = document.getElementById("select-all");
if (selectAll) {
    selectAll.addEventListener('click', (e) => {
        allSelected = !allSelected;
        document.querySelectorAll('.chkBattery').forEach(checkbox => {
            checkbox.checked = allSelected;
        });
        e.target.innerText = allSelected ? "☒" : "☑";
    });
}

// Filter table by battery ID
const filterById = document.getElementById("filterById")
if (filterById) {
    filterById.addEventListener('keyup', (e) => {
        const keyword = e.target.value.toLowerCase();

        const table = document.getElementById("tblBatteries");
        const tableRows = table.getElementsByTagName('tr');

        // Loop through all table rows, and hide those who don't match the search query
        for (let i=0; i < tableRows.length; i++) {
            const row = tableRows[i];
            const tdBatteryId = row.getElementsByTagName("td")[1];

            if (tdBatteryId) {
                const value = tdBatteryId.textContent || tdBatteryId.innerText;
                const found = value.toLowerCase().indexOf(keyword) > -1;
                if (found) {
                    row.classList.remove('hidden');
                } else {
                    row.classList.add('hidden');
                }
            }
        }
    });
}

// Delete selected battery ids
const btnDeleteSelected = document.getElementById('delete-selected');
if (btnDeleteSelected) {
    btnDeleteSelected.addEventListener('click', async (e) => {
        // Get only visible battery ids
        const selectedCheckboxes =
            document.querySelectorAll('tr:not(.hidden) .chkBattery:checked');
        const selectedIds = [].map.call(selectedCheckboxes, x => x.value);

        if (selectedIds.length > 0 && confirm('Confirm multiple delete?')) {
            const url = window.location.origin + "/batteries/delete"
            await sendRequest(url, 'POST', {ids: selectedIds});
            location.reload();
        }
    });
}

// Copy selected capacities to clipboard
const btnCopySelectedCapacities = document.getElementById('copy-selected-capacities');
if (btnCopySelectedCapacities) {
    btnCopySelectedCapacities.addEventListener('click', (e) => {
        const selectedBatteries =
            document.querySelectorAll('tr:not(.hidden) .chkBattery:checked');

        let capacities = '';
        selectedBatteries.forEach(selectedBattery => {
            const capacity = selectedBattery
                .parentNode
                .parentNode
                .querySelector('.capacity');

            if (capacity) {
                capacities += `${capacity.innerText} `;
            }
        });

        if (capacities) {
            copyToClipboard(capacities.trim());
            alert('Capacities copied to clipboard!');
        }
    });
}


// Helpers
async function sendRequest(url, type, body) {
    return fetch(url, {
        method: type,
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    });
}

function copyToClipboard(text) {
    const dummyTextarea = document.createElement('textarea');
    document.body.appendChild(dummyTextarea);
    dummyTextarea.value = text;
    dummyTextarea.select();
    document.execCommand('copy');
    document.body.removeChild(dummyTextarea);
  }
