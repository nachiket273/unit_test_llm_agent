import os


class CoverageAgent:
    def __init__(self, source_fp: str, test_fp: str,
                 num_iter: int = 5) -> None:
        try:
            self._check_file_paths(source_fp)
        except Exception as e:
            raise e

        self.source_fp = source_fp

        try:
            self._check_file_paths(test_fp)
        except Exception as e:
            raise e

        self.test_fp = test_fp
        self.num_iter = num_iter

    @classmethod
    def _check_file_paths(cls, path: str):
        if not os.path.exists(path):
            raise Exception(f"Path {path} does not exist")

        if not os.path.isfile(path):
            raise FileNotFoundError(f"File {path} does not found.")

        return
