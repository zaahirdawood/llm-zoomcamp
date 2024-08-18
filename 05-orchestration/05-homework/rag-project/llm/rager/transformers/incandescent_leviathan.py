import hashlib

def generate_document_id(doc):
    combined = f"{doc['course']}-{doc['question']}-{doc['text'][:10]}"
    hash_object = hashlib.md5(combined.encode())
    hash_hex = hash_object.hexdigest()
    document_id = hash_hex[:8]
    return document_id

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    documents = []

    if isinstance(data, list):
        for course_dict in data:
            for doc in course_dict['documents']:
                doc['course'] = course_dict['course']
                doc['document_id'] = generate_document_id(doc)
                documents.append(doc)
    elif isinstance(data, dict):
        for doc in data['documents']:
            doc['course'] = data['course']
            doc['document_id'] = generate_document_id(doc)
            documents.append(doc)
    else:
        raise ValueError(f"Unexpected data type: {type(data)}")

    print(len(documents))

    return documents

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'