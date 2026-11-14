from validations.output_schemas import output_schema

def validate_outputs(df):
    return output_schema.validate(df)
