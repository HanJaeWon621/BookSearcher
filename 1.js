Python.run(`
  def greet(name):
      return "Hello, " + name

  result = greet("John")
  result
`).then(console.log);
