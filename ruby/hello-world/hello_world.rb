class HelloWorld
  def self.hello *name
    "Hello, #{name == [] ? "World!" : name[0]+"!"}"
  end
end