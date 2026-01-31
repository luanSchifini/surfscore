import js from "@eslint/js";
import globals from "globals";

export default [
  js.configs.recommended,
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "commonjs", // Como você usa require/module.exports
      globals: {
        ...globals.node,    // Adiciona 'process', '__dirname', etc.
        ...globals.jest     // Adiciona 'describe', 'it', 'expect'
      },
    },
    rules: {
      "no-unused-vars": "warn", // Apenas avisa, não quebra o build por enquanto
      "no-console": "off"       // Permite console.log no backend
    },
  },
];