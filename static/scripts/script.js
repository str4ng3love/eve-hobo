import {
  UpdateBuyOrders,
  UpdateSellOrders,
  GetBuyOrdersReprocess,
  GetSellOrdersReprocess,
} from "./modules/APICalls.js";

import { ShowMessage } from "./modules/notifications.js";

const buyUpdate = document.getElementById("update-buy");
const sellUpdate = document.getElementById("update-sell");
const reproBuy = document.getElementById("repro-buy");
const reproSell = document.getElementById("repro-sell");


// //      Event Listeners

buyUpdate
  ? buyUpdate.addEventListener("click", async (e) => {
      let resp = await UpdateBuyOrders(e);
      ShowMessage(resp);
    })
  : null;
sellUpdate
  ? sellUpdate.addEventListener("click", async (e) => {
      let resp = await UpdateSellOrders(e);
      ShowMessage(resp);
    })
  : null;
// reproBuy
//   ? reproBuy.addEventListener("click", async (e) => {
//       const searchBy = e.target.parentElement.children[1].children[1].value;
//       const amount = e.target.parentElement.children[1].children[3].value;
//       if (amount.length == 0) {
//         ShowMessage({ error: "Input numeric value." });
//       }
//       let resp = await GetBuyOrdersReprocess(searchBy, amount);
//       ShowMessage(resp);
//     })
//   : null;
// reproSell
//   ? reproSell.addEventListener("click", async (e) => {
//       const searchBy = e.target.parentElement.children[1].children[1].value;
//       const amount = e.target.parentElement.children[1].children[3].value;
//       if (amount.length == 0) {
//         ShowMessage({ error: "Input numeric value." });
//       }
//       let resp = await GetSellOrdersReprocess(searchBy, value);
//       ShowMessage(resp);
//     })
//   : null;
