export async function UpdateBuyOrders() {
    let resp = await fetch('/api/esi-update-buy-orders')
    let data = await resp.json()
    return data

}




