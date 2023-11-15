document.addEventListener("DOMContentLoaded", function () {
    // !!! VARIABLES !!!
    const cpuRange = document.getElementById("cpu-range");
    const cpuRangeLabel = document.getElementById("cpu-range-label");

    const ramRange = document.getElementById("ram-range");
    const ramRangeLabel = document.getElementById("ram-range-label");

    const ssdRange = document.getElementById("ssd-range");
    const ssdRangeLabel = document.getElementById("ssd-range-label");

    const ssd2Range = document.getElementById("ssd2-range");
    const ssd2RangeLabel = document.getElementById("ssd2-range-label");

    const backupsRange = document.getElementById("backup-range");
    const backupsRangeLabel = document.getElementById("backup-range-label");

    const usuariosRange = document.getElementById("usuarios-range");
    const usuariosRangeLabel = document.getElementById("usuarios-range-label");

    const windowsBox = document.getElementById("windows");
    const dedicadaBox = document.getElementById("dedicada");
    const redBox = document.getElementById("red");
    const adminBox = document.getElementById("admin");


    const basicoButton = document.getElementById('basico-button');
    const medioButton = document.getElementById('medio-button');
    const proButton = document.getElementById('pro-button');



    // !!! ACTUALIZAR VALORES !!!

    cpuRange.addEventListener("input", () => {
        const value = parseInt(cpuRange.value, 10);
        cpuRangeLabel.textContent = value;
    });

    ramRange.addEventListener("input", () => {
        const value = parseInt(ramRange.value, 10);
        ramRangeLabel.textContent = value;
    });

    ssdRange.addEventListener("input", () => {
        const value = parseInt(ssdRange.value, 10);
        ssdRangeLabel.textContent = value;
    });


    ssd2Range.addEventListener("input", () => {
        const value = parseInt(ssd2Range.value, 10);
        ssd2RangeLabel.textContent = value;
    });

    backupsRange.addEventListener("input", function() {
        backupsRangeLabel.textContent = this.value;
    });

    usuariosRange.addEventListener("input", () => {
        const value = parseInt(usuariosRange.value, 10);
        usuariosRangeLabel.textContent = value;
    });

    windowsBox.addEventListener("change", () => {});

    dedicadaBox.addEventListener("change", () => {});

    redBox.addEventListener("change", () => {});

    adminBox.addEventListener("change", () => {});






    // !!! BOTONES !!!

    basicoButton.addEventListener('click', function () {
        // Define los valores predeterminados que deseas
        const cpuPro = 8; // Por ejemplo, 64
        const ramPro = 12;
        const ssdPro = 100;

        // Cambia el valor de los rangos de entrada y las etiquetas correspondientes
        cpuRange.value = cpuPro;
        cpuRangeLabel.textContent = cpuPro;

        ramRange.value = ramPro;
        ramRangeLabel.textContent = ramPro;

        ssdRange.value = ssdPro;
        ssdRangeLabel.textContent = ssdPro;

        updateTotalPrice();
    });

    medioButton.addEventListener('click', function () {
        // Define los valores predeterminados que deseas
        const cpuPro = 32; // Por ejemplo, 64
        const ramPro = 32;
        const ssdPro = 150;

        // Cambia el valor de los rangos de entrada y las etiquetas correspondientes
        cpuRange.value = cpuPro;
        cpuRangeLabel.textContent = cpuPro;

        ramRange.value = ramPro;
        ramRangeLabel.textContent = ramPro;

        ssdRange.value = ssdPro;
        ssdRangeLabel.textContent = ssdPro;

        updateTotalPrice();
        
    });

    proButton.addEventListener('click', function () {
        // Define los valores predeterminados que deseas
        const cpuPro = 64; // Por ejemplo, 64
        const ramPro = 65;
        const ssdPro = 250;

        // Cambia el valor de los rangos de entrada y las etiquetas correspondientes
        cpuRange.value = cpuPro;
        cpuRangeLabel.textContent = cpuPro;

        ramRange.value = ramPro;
        ramRangeLabel.textContent = ramPro;

        ssdRange.value = ssdPro;
        ssdRangeLabel.textContent = ssdPro;

        updateTotalPrice();
        
    });





    // !!! ACTUALIZAR PRECIO !!!
    const totalPriceElement = document.getElementById("total-price");


    // Funcion para actualizar el precio
    function updateTotalPrice() {
        const cpuValue = cpuRange.value;
        const ramValue = ramRange.value;
        const ssdValue = ssdRange.value;
        const ssd2Value = ssd2Range.value;
        const usuariosValue = usuariosRange.value;
        const backupsValue = backupsRange.value;
        const windowsChecked = windowsBox.checked;
        const dedicadaChecked = dedicadaBox.checked;
        const redChecked = redBox.checked;
        const adminChecked = adminBox.checked;


        fetch("calculate_price_view/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `cpu=${cpuValue}&ram=${ramValue}&ssd=${ssdValue}&ssd2=${ssd2Value}&usuarios=${usuariosValue}&backups=${backupsValue}&windows=${windowsChecked}&dedicada=${dedicadaChecked}&red=${redChecked}&admin=${adminChecked}`,
        })
            .then((response) => response.text())
            .then((data) => {
                totalPriceElement.textContent = `${parseFloat(data).toFixed(2)}€/mes`;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    // Listeners
    cpuRange.addEventListener("input", updateTotalPrice);
    ramRange.addEventListener("input", updateTotalPrice);
    ssdRange.addEventListener("input", updateTotalPrice);
    ssd2Range.addEventListener("input", updateTotalPrice);
    backupsRange.addEventListener("input", updateTotalPrice);
    usuariosRange.addEventListener("input", updateTotalPrice);
    windowsBox.addEventListener("change", updateTotalPrice);
    dedicadaBox.addEventListener("change", updateTotalPrice);
    redBox.addEventListener("change", updateTotalPrice);
    adminBox.addEventListener("change", updateTotalPrice);




});