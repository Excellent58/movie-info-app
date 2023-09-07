/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        bc: "#050D21",
        primary: "#FFFDFB",
        secondary: "#B46CF8",
        danger: "#1A67F8",
        lightGrey: "#C9D5EE",
      },

      fontFamily: {
        raleway: ["Raleway", "sans-serif"],
      },
    },
  },
  plugins: [],
}

