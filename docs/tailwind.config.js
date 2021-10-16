module.exports = {
    purge: {
        content: ["*.html", "js/main.js"],
    },
    darkMode: false, // or "media" or "class"
    theme: {
        extend: {
            colors: {
                "gray-primary": "#191919",
                "gray-secondary": "#2f2f30",
                "gray-divider": "#292929"
            },
            fontFamily: {
                sans: ["Inter", "system-ui", "sans-serif"],
            },
        }
    },
    variants: {
        extend: {},
    },
    plugins: [],
};
