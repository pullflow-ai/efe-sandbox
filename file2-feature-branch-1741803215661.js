// JavaScript Example

function greet(name) {
  return `Hello, ${name}!`;
}

// Example usage
console.log(greet("GitHub"));

// Error handling example
function safeGreet(name) {
  if (typeof name !== "string") {
    throw new Error("Name must be a string");
  }
  return greet(name);
}