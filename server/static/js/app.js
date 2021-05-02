// Un/Select all batteries
const selectAll = document.getElementById("select-all");
if (selectAll) {
    selectAll.addEventListener('click', (e) => {
        let allSelected = true;
        document.querySelectorAll('.chkBattery').forEach(checkbox => {
            checkbox.checked = !checkbox.checked;
            allSelected = checkbox.checked;
        });

        e.target.innerText = allSelected ? "✘" : "✔";
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
                row.style.display = found ? "" : "none";
            }
        }
    });
}
