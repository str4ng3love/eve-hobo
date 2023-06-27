export function ShowMessage(message) {
  const prevNotifications = Array.from(
    document.querySelectorAll(".notifications-container")
  );

  let latestZIndex = 1
  if (prevNotifications.length > 0) {
    latestZIndex = latestZIndex + prevNotifications.length
  }

  const main = document.querySelector("main");
  const container = document.createElement("div");
  const para = document.createElement("p");
  container.classList.add("notifications-container");
  para.innerHTML = message.error || message.message;
  container.style.zIndex = latestZIndex
  container.appendChild(para);
  main.insertAdjacentElement("afterend", container);
  setTimeout(() => {
    container.style.opacity = 1;
  }, 0);
  setTimeout(() => {
    container.style.opacity = 0;
  }, 4500);
  setTimeout(() => {
    container.remove();
  }, 5000);
}
