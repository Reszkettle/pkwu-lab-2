# Routes

You'll find here the routes exposed by this repository. Note that you can also review them through the interactive API docs. The interactive API docs are located at `/docs` and `/redoc`

## String router

### **Analyse string**

#### GET `/analyse-string`

#### **Description**:

Analyzes the given string counting the number of uppercase and lowercase letters, digits and special characters. Optionally, if substring is given, also counts the number of times that substring occurs in the given string.

#### **Request Body**

| Type     | Name      | Optional | Description                                          |
| -------- | --------- | -------- | ---------------------------------------------------- |
| `string` | string    | No       | string that will be analyzed                         |
| `string` | substring | Yes      | optional substring which occurrences will be counted |

### Response

On success (HTTP 200 status) this endpoint returns following Response Body

#### **Response Body**

| Type  | Name                        | Optional | Description                            |
| ----- | --------------------------- | -------- | -------------------------------------- |
| `int` | lower_case_letters_count    | No       | number of lowercase letters in string  |
| `int` | upper_case_letters_count    | No       | number of uppercase letters in string  |
| `int` | digits_count                | No       | number of digits in string             |
| `int` | special_characters_count    | No       | number of special characters in string |
| `int` | substring_occurrences_count | Yes      | number of substring occurences         |
