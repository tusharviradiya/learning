# validations

- Serializer validation:You can specify validators for individual fields in a serializer. For example, you might specify that a field must be a certain length or must meet a certain pattern.
- Form validation:You can use Django's built-in form validation by creating a Form class and using it to validate input data.
- Model validation:If you are using Django models to store your data, you can use Django's built-in model validation to check that the input data is valid. This includes checking for unique constraints and foreign key relationships.
- Custom validation:In addition to the above techniques, you can also define your custom validation logic to check for more complex conditions.

# validation in serializer
- convert data from Python objects into a format that can be easily rendered into JSON or parsed from incoming JSON requests. This aspect is particularly crucial when dealing with APIs, as the standard practice involves the exchange of data in JSON format
