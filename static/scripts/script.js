import {
  UpdateBuyOrders,
  UpdateSellOrders,
  GetOrders,
} from "./modules/APICalls.js";
import { ShowMessage } from "./modules/notifications.js";

const salvagerBtn = document.getElementById("salvager-btn");
const resultsBtn = document.getElementById("results-btn");
const buyUpdate = document.getElementById("update-buy");
const sellUpdate = document.getElementById("update-sell");
const reproSubmitBtn = document.getElementById("repro-submit");

// //      Event Listeners
salvagerBtn
  ? salvagerBtn.addEventListener("click", (e) => {
      const salvagerId = document.getElementById("salvager-id");
      const resultsId = document.getElementById("results-id");
      salvagerId.classList.add("top");
      resultsId.classList.remove("top");
    })
  : null;

resultsBtn
  ? resultsBtn.addEventListener("click", (e) => {
      const salvagerId = document.getElementById("salvager-id");
      const resultsId = document.getElementById("results-id");
      salvagerId.classList.remove("top");
      resultsId.classList.add("top");
    })
  : null;

reproSubmitBtn
  ? reproSubmitBtn.addEventListener("submit", async (e) => {
      e.preventDefault();
      const orders_type = e.target.children[0].children[1].value;
      let orders = await GetOrders(orders_type);
      ShowMessage({'message':`Downloaded ${orders.length} orders... \nProcessing...`})
      
      
    })
  : null;

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
