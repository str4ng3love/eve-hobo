import { UpdateBuyOrders } from "./modules/APICalls.js"


let update = document.getElementById('update-buy')






// Events Listeners

if(update)
    update.addEventListener("click", (e)=> {UpdateBuyOrders(e)})