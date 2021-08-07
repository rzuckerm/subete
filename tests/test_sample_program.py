from subete import SampleProgram

TEST_FILE_NAME = "hello_world.py"
TEST_FILE_PATH = "tests/python/"
TEST_LANG = "Python"


def test_sample_program_str():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert str(test) == "Hello World in Python"


def test_sample_program_language():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.language() == TEST_LANG


def test_sample_program_code():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.code() == 'print("Hello, World!")\n'


def test_sample_program_line_count():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.line_count() == 1


def test_sample_program_size():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.size() > 0


def test_sample_program_requirements_url():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.requirements_url() == "https://sample-programs.therenegadecoder.com/projects/hello-world"


def test_sample_program_documentation_url():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.documentation_url() == "https://sample-programs.therenegadecoder.com/projects/hello-world/python"


def test_sample_program_issue_query_url():
    test = SampleProgram(TEST_FILE_PATH, TEST_FILE_NAME, TEST_LANG)
    assert test.article_issue_query_url() == "https://github.com//TheRenegadeCoder/sample-programs-website/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+hello+world+python"