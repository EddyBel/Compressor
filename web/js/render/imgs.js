function RenderIMGS(imgs) {
  ELEMENTS.ContainerListImgs.innerHTML = "";

  for (let i = 0; i < imgs.length; i++) {
    const img = imgs[i];
    const name = img.name;
    const size = (parseInt(img.size) / 1024).toFixed(2);
    const type = img.type;
    const url = URL.createObjectURL(img);

    ELEMENTS.ContainerListImgs.innerHTML += `
   <li class="py-3 sm:py-4">
          <div class="flex items-center space-x-4">
            <div class="flex-shrink-0">
              <img
                class="w-8 h-8 rounded-full"
                src="${url}"
                alt="Neil image"
              />
            </div>
            <div class="flex-1 min-w-0">
              <p
                class="text-sm font-medium text-gray-900 truncate dark:text-white"
              >
                ${name}
              </p>
              <p class="text-sm text-gray-500 truncate dark:text-gray-400">
                ${type}
              </p>
            </div>
            <div
              class="inline-flex items-center text-base font-semibold text-gray-900 dark:text-white"
            >
              ${size} Kb
            </div>
          </div>
  </li>
  `;
  }
}
