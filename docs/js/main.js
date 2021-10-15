"use strict";

// Setup and connect sliders
let rangeslider;
let iconsContainer = document.getElementById("icons-container");
let searchBar = document.getElementById("searchBar");
let searchBarContainer = document.getElementById("searchBarContainer");
let propertiesContainer = document.getElementById("propertiesContainer");
let downloadBtnsContainer = document.getElementById("downloadBtnsContainer");
let tagsContainer = document.getElementById("tagsContainer");
let searchBarOffset = searchBarContainer.offsetTop;
let propertiesOffset = propertiesContainer.offsetTop;
let iconSVGTextContent = "";
let iconFileName = "";
let counter = 0;
window.addEventListener("load", function () {
  var config = {
    min: 75,
    max: 200,
    onRangeChange: function (slider) {
      document
        .querySelectorAll("#icons-container button div")
        .forEach(function (element) {
          element.style["transform"] = `scale(${slider.currentRange}%)`;
        });
    },
    afterInit: function (slider) {
      slider.setRange(100);
    },
  };
  rangeslider = RangeSlider.create("#icon-size-slider", config);
  // Setup searchbar
  try {
    displayIcons(iconsList);
  } catch (err) {
    console.error(err);
    message("Sorry, icons could not be loaded - try reloading the page.");
  }
});

function message(value) {
  toast = document.getElementById("toast");
  clearTimeout(message.timer);
  if (toast.hidden) {
    toast.textContent = value;
  } else {
    toast.textContent += "\n" + value;
  }
  toast.hidden = false;
  message.timer = setTimeout(function () {
    toast.hidden = true;
  }, 1500);
}

function insertAfter(newNode, existingNode) {
  existingNode.parentNode.insertBefore(newNode, existingNode.nextSibling);
}

// Credits to https://www.bitdegree.org/learn/javascript-download
function download(filename, svg) {
  var element = document.createElement("a");
  element.setAttribute(
    "href",
    "data:image/svg+xml;charset=utf-8," + encodeURIComponent(svg)
  );
  element.setAttribute("download", filename);
  element.style.display = "none";
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}

// This is the main search function
// It takes the icons dict (with > 600 icons) as input
// to display the icon grid
function displayIcons(icons) {
  const htmlString = icons
    .map(function (icon) {
      return `
         <button class="flex flex-col mx-1 my-3 rounded-lg focus:ring-4 focus:ring-gray-divider focus:outline-none" id="${
           icon.label
         }" data-icon-btn="1" data-height="${icon.height}" data-width="${icon.width}" data-tags="${icon.tags.join(" ")}" data-index="${icons.indexOf(icon)}">
             <!--${icon.label} icon SVG code-->
             <div class="flex justify-center px-4 py-6">
                 <svg class="w-12 h-12 icon blender" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg">
                     ${icon.markup}
                 </svg>
             </div>
             <!--${icon.label} icon name-->
                 <span class="overflow-hidden px-2 pb-3 w-32 text-sm text-center overflow-ellipsis">${
                   icon.label
                 }</span>
         </button>`;
    })
    .join("");
  iconsContainer.innerHTML = htmlString;
}

searchBar.addEventListener("keyup", function (e) {
  const searchString = e.target.value.toLowerCase();
  const filteredIconsList = iconsList.filter(function (icon) {
    return (
      icon["label"].toLowerCase().includes(searchString) ||
      icon["tags"][0].toLowerCase().includes(searchString)
      // TODO: add ability to search through all tags
      // rather than just the first tag
    );
  });
  displayIcons(filteredIconsList);
});

document
  .getElementById("slider-reset-btn")
  .addEventListener("click", function () {
    message("✅ Size reset to default!");
    rangeslider.setRange(100);
  });

// Sticky search bar
window.onscroll = function () {
  if (window.pageYOffset > searchBarOffset) {
    searchBarContainer.classList.add("sticky-el");
    propertiesContainer.classList.add("sticky-el");
  } else {
    searchBarContainer.classList.remove("sticky-el");
    propertiesContainer.classList.remove("sticky-el");
  }
};

// Properties editor state system
let propertiesEditor = document.getElementById("propertiesContainer");
let state = {
  icon_selected: false,
  clicked_blank_area: false,
};

let template = function (iconName, tagsArray, iconIndex) {
  // If an icon is selected
  if (state.icon_selected) {
    // HTML markup for tags dynamically generated
    // and placed in variable $tagsMarkup
    let tagsMarkup = "";
    tagsArray.forEach(function (tag) {
      tagsMarkup += `<span class="px-4 py-1 m-1 text-sm font-medium leading-loose rounded-lg bg-gray-secondary">${tag}</span>\n`;
    });
    iconName = "Icon: " + iconName + ".svg";
    // This will be used for both copying and downloads
    iconSVGTextContent = `<svg class="w-12 h-12 icon blender" height="20" viewBox="0 0 24 24" width="20" xmlns="http://www.w3.org/2000/svg">
            ${iconsList[iconIndex]["markup"]}
        </svg>`;
    iconFileName = iconsList[iconIndex]["filename"];
    return `
            <h1 class="mb-5 text-xl font-medium text-gray-400">Properties</h1>
            <div id="downloadBtnsContainer" class="flex flex-col py-10 space-y-5">
                <!--Label for icon name-->
                <h2 class="font-medium text-gray-400 text-md">${iconName}</h2>
                <!--Buttons container-->
                <div class="flex flex-col space-y-3">
                    <!--Copy icon button-->
                    <button id="cp-icon-btn" class="flex justify-center px-6 py-3 bg-none rounded-md border border-gray-300 transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-105 hover:bg-black">
                        <div class="flex flex-row space-x-1 text-gray-300">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                            </svg>
                            <span class="text-sm font-medium">Copy Icon</span>
                        </div>
                    </button>
                    <!--Download SVG button-->
                    <button id="download-icon-btn" class="flex justify-center px-6 py-3 rounded-md transition duration-500 ease-in-out transform bg-gray-secondary hover:scale-105 hover:bg-black">
                        <div class="flex flex-row space-x-1 text-gray-300">
                            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                            </svg>
                            <span class="text-sm font-medium">Download SVG</span>
                        </div>
                    </button>
                </div>
            </div>
            <div id="tagsContainer" class="flex flex-col py-10 space-y-5">
                <!--Label for tags-->
                <h2 class="font-medium text-gray-400 text-md">Tags</h2>
                <!--List of tags here-->
                <div class="flex flex-wrap text-gray-400">
                    ${tagsMarkup}
                </div>
            </div>`;
  } else {
    return `
            <div>
                <h1 class="mb-5 text-xl font-medium text-gray-400">Properties</h1>
                <p class="text-gray-400 text-md">Please select an icon to view its properties</p>
            </div>
        `;
  }
};

function render(iconName, tagsArray, iconIndex) {
  if (!iconName) {
    iconName = "name not known";
    tagsArray = ["Array not found"];
    iconIndex = 0;
  }
  propertiesEditor.innerHTML = template(iconName, tagsArray, iconIndex);
}

// We will re-call this function every time we need to make changes
// Event delegation for clicks that will re-render UI
// Known issue: the properties panel suddenly disappears
// once the "Copy" or "Download" buttons are clicked
// TODO: fix disappearing properties panel on click bug
document.addEventListener(
  "click",
  function (event) {
    // Check what we click
    let isValidEvent = event.target.dataset.iconBtn === "1";
    if (isValidEvent) {
      console.log("Valid!");
      let iconName = event.target.id;
      let tagsArray = event.target.dataset["tags"].split(" ");
      let iconIndex = event.target.dataset["index"];
      state.clicked_blank_area = false;
      state.icon_selected = true;
      propertiesContainer.classList.add("divide-y", "divide-gray-divider");
      render(iconName, tagsArray, iconIndex);
      // Event listeners for the download and copy buttons
      document.getElementById("cp-icon-btn").addEventListener(
        "click",
        function () {
          message("✅ Copied icon!");
          navigator.clipboard.writeText(iconSVGTextContent);
        },
        false
      );
      document.getElementById("download-icon-btn").addEventListener(
        "click",
        function () {
          message("✅ SVG download in progress!");
          download(iconFileName, iconSVGTextContent);
        },
        false
      );
      // We want this to also run if the currently selected
      // element changes
      event.target.addEventListener("blur", function () {
        state.icon_selected = false;
      });
    } else {
      state.clicked_blank_area = true;
      render();
    }
  },
  false
);

// Of course we are also rendering the dynamic UI on load
window.addEventListener(
  "load",
  function () {
    render();
  },
  false
);