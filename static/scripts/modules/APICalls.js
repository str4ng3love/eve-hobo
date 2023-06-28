export async function UpdateBuyOrders() {
  let resp = await fetch("/api/esi-update-buy-orders");
  let data = await resp.json();
  return data;
}
export async function UpdateSellOrders() {
  let resp = await fetch("/api/esi-update-sell-orders");
  let data = await resp.json();
  return data;
}
export async function GetBuyOrdersReprocess(searchBy, amount) {
  const resp = await fetch(`/api/reprocess/buy/${searchBy}/${amount}`);
  const data = await resp.json();
  return data;
}
export async function GetSellOrdersReprocess() {
  const resp = await fetch(`/api/reprocess/sell/${searchBy}/${amount}`);
  const data = await resp.json();
  return data;
}
