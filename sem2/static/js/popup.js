var modal = document.getElementById("myModal");

var info = document.getElementById("information");

// When the user clicks on the button, open the modal
function showInfo(location) {

    switch (location) {
        case 1:
            info.textContent = "Displays the current vibration intensity over the threshold value. This area will change in color from green to yellow to red, in ascending order of vibration value.";
            break;
        case 2:
            info.textContent = "Displays the current number of visitors to the library, with the maximum crowd size being 99. Helps library staff control crowd size. This area will change in color from green to yellow to red, in ascending order in accordance to the crowd level.";
            break;
        case 3:
            info.textContent = "Displays the current brightness percentage of the lights in the library, which is controlled by a pot click.";
            break;
        case 4:
            info.textContent = "Displays the current noise level over the threshold value. Noise level varies from level 1 to 4, in ascending order. This area will change in color from green to yellow to red, in ascending order of noise level.";
            break;
        case 5:
            info.textContent = "Shows the 10 most recent vibration readings, along with the current status."
            break;
        case 6:
            info.textContent = "Shows the 30 most recent visitor trends, which allow library staffs to predict peak periods."
            break;
        case 8:
            info.textContent = "Allows staff to change the vibration threshold. When the vibration reading goes beyond the threshold, the warning will be activated."
            break;
        case 9:
            info.textContent = "Allows staff to change the number of visitors counted, which will be reflected in 'Number of Visitors' counter above."
            break;
        case 10:
            info.textContent = "Support Options to allow specialists to troubleshoot.";
            break;
        default:
            info.textContent = location;
            break;
    }
    modal.style.display = "block";

}

function closeInfo() {
    modal.style.display = "none";
}