Complete the following methods.

In the class `TestDataEmptyArray`:

- `get_array()` returns an empty array

In the class `TestDataUniqueValues`:

- `get_array()` returns an array of size at least 2 with all unique elements
- `get_expected_result()` returns the expected minimum value index for this array

In the class `TestDataExactlyTwoDifferentMinimums`:

- `get_array()` returns an array where the minimum value occurs at exactly 2 indices
- `get_expected_result()` returns the expected index
  Take a look at the code template to see the exact implementation of functions that your colleague already implemented.

Note: The arrays are indexed from `0`.

### solution.py

```python
class TestDataEmptyArray():
    def get_array():
        return []


class TestDataUniqueValues():
    def get_array():
        return [1, 2, 3]

    def get_expected_result():
        return 0


class TestDataExactlyTwoDifferentMinimums():
    def get_array():
        return [1, 1, 2]

    def get_expected_result():
        return 0
```

> Unit 테스트를 위한 Python 코드 만들기
>
> 1. 빈 List
> 2. 모든 요소가 유일한 List
> 3. 가장 작은 요소가 중복인 List
