# Table of Contents:
---

1. MS Power Automate, Lists, and Forms
2. JSON 101

---
# Working with Microsoft Flow, Lists, and MS Form 
---
## Quick Notes & Resources

> Microsoft uses PowerFX as the "new" language behind the Power Automate platform

- **Note**: you can get the _field name_ (for MS Flow) from MS List > List > List Settings > Desired Column. Then get everything after _Field=_ in the URL
- **Note**: list is limited to 5000 "view" items

- [YouTube - Intro to the PowerApps If Statement](https://www.youtube.com/watch?v=9aXP48XECDc)
- [Microsoft - Get Form Response Details as JSON](https://powerusers.microsoft.com/t5/General-Power-Automate/get-form-response-details-as-json/td-p/61065)
- [Microsoft - Use Parse JSON action in Power Automate](https://techcommunity.microsoft.com/t5/microsoft-365-pnp-blog/how-to-use-parse-json-action-in-power-automate/ba-p/2121861)
- [YouTube - Power Automate and JSON Property Name with Special Character](https://www.youtube.com/watch?v=S5eqq3KjaBI)
- [Code Beautify](https://codebeautify.org/jsonviewer)
- [Power Automate Syntax](https://docs.microsoft.com/en-us/power-automate/use-expressions-in-conditions)
- [Power Automate OData Filter Query flow for SharePoint list](https://www.youtube.com/watch?v=yeAnuTB85eg)

---


## Power Automate (PowerFX) Syntax Examples

<table>
  <tr>
    <th>Syntax</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>if(expression, valueIfTrue, valueIfFalse)</td>
    <td>returns a specific value if the expression results in true or false</td>
  </tr>
  <tr>
    <td>and(exp_1, exp_2, exp_n)</td>
    <td>returns true if both parameters are true</td>
  </tr>
  <tr>
    <td>or(exp_1, exp_2, exp_n)</td>
    <td>returns true if any parameters are true</td>
  </tr>
  <tr>
    <td>contains(collection, value)</td>
    <td>returns true if a dictionary contains a key, if an array contains a value, or if a string contains a substring</td>
  </tr>
  <tr>
    <td>equals(object_1, object_2)</td>
    <td>returns true if two values are equal</td>
  </tr>
  <tr>
    <td>array(value)</td>
    <td>convert the input to an array</td>
  </tr>
  <tr>
    <td>outputs(actionName)</td>
    <td>shorthand for actions('actionName'); `'Get_response_details'` is an example</td>
  </tr>
  <tr>
    <td>actions(actionName)</td>
    <td>enables an expression to derive its value from other JSON name and value pairs or the output of the runtime action</td>
  </tr>
  <tr>
    <td>?</td>
    <td>used with JSON; specifies that if the field being referenced does not exist then a NULL value will be returned</td>
  </tr>
  <tr>
    <td>not()</td>
    <td>returns the opposite of the boolean value in the internal expression</td>
  </tr>
</table>

### Examples

- `if(contains('coding is awesome', 'is awesome'))` equals **true**
- `if(equals('my name is fred', 'my name is ed'))` equals **false**
- `not(contains('200 Success', 'Fail'))` equals **true**; the `contains()` statement itself is false so putting `not()` returns the opposite value

---

## Create MS Flow to Automate MS Form (Quiz) to MS List

> This _How-To_ will walk through the creation of a Microsoft Flow that communicates data between a Form submission and a List we create. This is for a quiz **not** a feedback form so it will "grade" the answers with either a 1 (correct) **or** a 0 (incorrect).

### Example Form/ JSON Output

- Example form link (Empower Scavenger Hunt): `iJ9HGayO0kWhv2nTOFSj-v1voxwn3WxFgr3nY_VFiv5URUkxU1BXSkNORTJLUDFDQTE0SDRIR1FXSC4u`
- JSON output for all **correct** responses on the Scavenger Hunt MS Form

```json
{
	"responder":"mfiles@loandepot.com",
	"submitDate":"6/25/2021 8:52:02 PM",
	"rb1801e3b38fc47d697d0a4510d49163c":"Dashboard > Key Dates Tab > Processing Dates Tab",
	"r6dc981fc90e945a49cd1f9d80399065b":"Alias Information",
	"ra9da2740025548e69261d293c892048e":"Vesting Information",
	"r1919d9d3f20f475cbce6fca36bd859ad":"DOT Screen",
	"r245ea1ec3ec2405b8532520f72de4ca9":"Loan Status",
	"rebf784f75cfe40a8ab04779966387fd6":"eConsent",
	"r0ef9681727ba448d9c422199a55d5d24":"Product Modeler (PROMO)",
	"r6d874fbdb25249f9a841fbf80dd70119":"Pricing Lock/History",
	"rfa466009520c4e9e8380059eefa2025e":"Escrow Account Input Screen",
	"r8a5e750ed2834c09a42c12ba720a0beb":"Contact Information Screen",
	"r8c83d1e5583647eda1a07fbe92959db2":"Fees Screen",
	"r801c12b6f217420eb27f89a18b7e4b61":"Closing Details screen",
	"rf0145151888b4a7bb5280730f5fb8ca1":"Section 4 of the 1003 or Property Information ",
	"r2f5aaec917124e95bb59268236895631":"Realtor Information screen",
	"r53535a687b78412fba41a579fad2674a":"Loan Disclosure>Fees Tab",
	"r03a7364d44cc435bb6ac45604a392ff8":"Contact Information screen",
	"r1e51f17fcee84e1ca48892fad701a185":"PROMO, Loan Summary screen and Dashboard",
	"r4085629b6a174657abeabde5e8476271":"Loan Summary & Housing/Debt Ratios",
	"r2b652fb8f49f415f93423ddd1aab6429":"All of the Above",
	"rfa91bb7518ee40a9a522eed89ed619a1":"PROMO",
	"ra5d9ab1df4fa4c1687d2813f24c6494c":"Workflow Validation",
	"r8bf6ff8991614e5bbee5f9fac6b624db":"Business Card Directory",
	"rfb3c2ccf2e6e4b2fb46a284d503704b0":"Yes, I understand",
	"rdb30658402c6443581d3972b240d0b89":"Reminder: Use your YODA resources and/or Empower TN1 Test Loan to help answer the questions"
}
```

### List Creation

> The instructions to create a new list is below. However, if you would prefer to work with a template then go to https://www.office.com/?auth=2 and open up the Lists app. Create a new list from an existing list and scroll to Training and Development then select _TEMPLATE - Quiz Results_ and modify as necessary to help expedite the process. Just make sure to update the Total Points and Final Result calculation when the number of questions has been determined/updated in the list accordingly.

1. Community Hub -> Training and Development -> New “List”
    - Type in Name and Details
    - Unclick “Show In-Site Navigation”
2. Columns
    - Change "Title" to “Submission Date”
    - Add "Quiz Month" as Type: Calculated
      - Formula: `=TEXT([Title], "mmmm")`
    - Add "Quiz Year" as Type: Calculated
      - Formula: `=TEXT([Title], "yyyy")`
    - Add “Employee Name” as Type: Person
    - Add "Total Points" as Type: Calculated
      - Formula: Add all of the numerical fields:

```jsx
= [Q1 - Points] + [Q2 - Points] + [Q3 - Points] + [Q4 - Points] + [Q5 - Points] + [Q6 - Points] + [Q7 - Points]
+ [Q8 - Points] + [Q9 - Points] + [Q10 - Points] + [Q11 - Points] + [Q12 - Points] + [Q13 - Points]
+ [Q14 - Points] + [Q15 - Points] + [Q16 - Points] + [Q17 - Points] + [Q18 - Points] + [Q19 - Points]
+ [Q20 - Points] + [Q21 - Points] + [Q22 - Points]
```

2. **continued**
      - Data type returned: Number
      - Number of decimal places: 0
    - Add "Final Result (%)" as Type: Calculated
      - Equation: `=ROUND((([Total Points]/22)*100),4)` where "22" equals the total number of points a trainee can score
      - Data type returned: Number
      - Number of decimal places: 2
      - Show as percentage: True
    - Add remaining columns (to match the MS Form questions - Does not need to be verbatim) as Type: Choice, Multiple Line of Text, etc
      - In this scenario you should add each as a numerical type and use the name format of Q<#> - Points (i.e., _Q1 - Points_)
3. Click Integrate -> Power Automate -> Create a Flow -> Show More -> See more templates

**NOTE**: Due to software issues (with regards to reporting), the _Title_ (Submission Date) column cannot be hidden so I find it best to bury it all the way to the right side of the list.
**NOTE**: Make sure to save to Training and Development when creating a new list. Uncheck _Show in Site Navigation_.
**NOTE**: You can add _Conditional Formatting_ to the Points columns using an _If ... equal to 1, then green_ **and** _If ... equal to 0, then red_. As far as the Final Result column, I used three separate formatting rules:
  - `If Final Result (%) is less than 0.65 Then Red`
  - `If Final Result (%) is between 0.65 and 0.79 Then Yellow`
  - `If Final Result (%) is greater than 0.79 Then Green`

### Flow Creation Part One: Dud Flow

> In order to create a flow that feeds quiz data into a list from a form, assuming we have the table set-up to capture just the numeric value, we need to create a flow that gives us the JSON data for the correct responses.

1. Search for “Record form responses in SharePoint”
    - Make sure the “This form will connect to:” box has two green check-marks next to the email addresses.
    - Click Continue
2. For the "dud" flow we need to delete the _Create Item_ command under the _Apply to each_, but we are using the remaining structure of the template we selected above.
3. Click Form ID -> Enter Custom Value (both locations)
    - URL of Form (example): https://forms.office.com/Pages/DesignPage.aspx?auth_pvr=OrgId&auth_upn=mfiles%40loandepot.com&lang=en-US&origin=OfficeDotCom&route=Start#FormId=iJ9HGayO0kWhv2nTOFSj-oNpoUByOl9Iq-XrRtAyVBVUNzUwWE9ZSjNVRDkzV1lZTkZTVUw2UFJEMiQlQCN0PWcu
    - Input everything in URL **after** _FormId=_
4. Under _Apply to each_ add a command _Send an email (V2)_
    - To: Your email
    - Subject: Whatever you want
    - Body: the following code: `body('Get_response_details')` **unless** it allows you to select _Body_
5. Save
6. Complete the form submission (on the applicable form) where you complete **all** correct responses
7. Open the email sent to you with the JSON data (we will need it shortly)

### Flow Creation Part Two: Actual Flow

> Now we are going to create the actual flow that should connect the dots between the quiz form and the list we created earlier. At this point you can delete the "dud" flow we previously created **or** edit and apply these steps to that one as we do not need it anymore because we do not want to receive emails every time a trainee completes that quiz.

**NOTE**: The data sent via email (JSON data) does **not** come through in the exact order that the quiz goes in so it needs to be reordered accordingly when building into the Flow.

1. Search for “Record form responses in SharePoint”
    - Make sure the “This form will connect to:” box has two green check-marks next to the email addresses.
    - Click Continue
2. Click Form ID -> Enter Custom Value (both locations)
    - URL of Form (example): https://forms.office.com/Pages/DesignPage.aspx?auth_pvr=OrgId&auth_upn=mfiles%40loandepot.com&lang=en-US&origin=OfficeDotCom&route=Start#FormId=iJ9HGayO0kWhv2nTOFSj-oNpoUByOl9Iq-XrRtAyVBVUNzUwWE9ZSjNVRDkzV1lZTkZTVUw2UFJEMiQlQCN0PWcu
    - Input everything in URL **after** _FormId=_
3.  Create item fields:
    - Title: Submission time
    - Employee Name 'Claims': Responders' Email Address
    - Total Points: Leave blank **if** present otherwise disregard
    - All other question "Points" fields -> Expression:
      - This is where you will need to add the appropriate If/Then statement. Per the example below, where **JSON_KEY** is the JSON ID (_key_) (i.e., "rb1801e3b38fc47d697d0a4510d49163c") and **ANSWER** / **FIRST_ANSWER** is/are the JSON _value(s)_ (i.e.,"'Dashboard > Key Dates Tab > Processing Dates Tab'") in the _key/ value_ pair for each question in the email we had sent to us earlier. The _key_ and _value_ needs to be swapped out for each value in the JSON return that is in the email.:

```jsx
// LOGIC ONE - String Literal
// For Radio-Button
If(equals(
  outputs('Get_response_details')?['body/<JSON_KEY>'],'<ANSWER>'),
  1, 0)
// For Check-Box
If(equals(
  outputs('Get_response_details')?['body/<JSON_KEY>'], '["<ANSWER>"]'), 1, 0)

// LOGIC TWO - Contains
If(and(
  contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<FIRST_ANSWER>'),
  contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<SECOND_ANSWER>')),
  1, 0)

// LOGIC THREE - Contains
If(and(
  contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<FIRST_ANSWER>'),
  contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<SECOND_ANSWER>')),
    If(or(
      contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<FIRST_WRONG_RESPONSE>'),
      contains(outputs('Get_response_details')?['body/<JSON_KEY>'], '<SECOND_WRONG_RESPONSE>')),
      0, 1),
    0)
```


**NOTE**: If you need to troubleshoot answers in a scenario where multiple questions have the same answer, then add a dud field to the list as a "Choice" type then create the Flow where you add the question field that pops-up when you click in the appropriate Flow field and click "Enter Custom Value". That way you can hover over the retrieved response and look at the JSON identifier in the pop-up clue.

**NOTE**: If you have a string with an apostrophe in it like, "I can't", the apostrophe needs to be _escaped_ in order to work properly. Apostrophes are _escaped_ with an additional apostrophe in front of it.

**NOTE**: In a scenario where you have a multiple-choice and the JSON output is:
```jsx
"rae7e8edba7974712add595254c8be0f6":"[\"Name as vested on title\",\"In Title box checked\",\"Email\",\"Mailing Address\"]"
```
Where the _key_ is "rae7e8edba7974712add595254c8be0f6" and the _value_ is "[\"Name as vested on title\",\"In Title box checked\",\"Email\",\"Mailing Address\"]" you **cannot** simply copy and paste the _value_ as it stands as there are JSON _escape_ characters in there that Microsoft will not register properly. So we need to update the If/Then statement (from above) to reflect the following:
```jsx
If(equals(outputs('Get_response_details')?['body/rae7e8edba7974712add595254c8be0f6'],
'["Name as vested on title","In Title box checked","Email","Mailing Address"]'), 1, 0)
```
Where the back-slashes are no longer in the answer.

### Importing the Old Data

> For this you ultimately need to open the Excel spreadsheet of the older data and format the data (remove columns) to match the list you previously created **prior to** copying then pasting the data over.

- Delete ID, Start time, Email, Total Points (this is calculated in the spreadsheet), any Quiz Feedback, all questions, all answers, **and** the dud (pointless) questions at the beginning/end (as applicable).
- Add back a **blank** column for _Total Points_ **and** _Final Resultss (%)_ as we need these strictly for placeholders
- Format the date/time with a _custom_ format of: `m/dd/yyyy h:mm:ss AM/PM` to match that of what the Flow feeds into the List

1. Go to List
2. Edit in Grid View
3. Select all data (**not** including header values) from cleaned up Excel then CTRL + C
4. Add new Item in List
5. Click the first empty box, scroll horizontally to the end and SHIFT + Click the last field
6. CTRL + V

**NOTE**: You need to wait until all rows populate over and run applicable calculations before closing out of the tab/window or trying to exit the grid view. Also, some trainee's names do not match up either because there was a typo or they are no longer with the company. Research in the email repository to figure out if they are with the company anymore and type in the correct name else just place your name then delete all entries with your name after the import is complete.

---

## Create MS Flow to Automate MS Form (Attestation) to MS List

> This _How-To_ will walk through the creation of a Microsoft Flow that communicates data between a Form submission and a List we create. This is for the activity attestation **not** a feedback form **or** a quiz.

- Create a MS List
  - Create the following fields:
    - Title (automatically included); renamed to "Record Creation Date"
    - Trainee
      - Require that this column contains information
      - Enforce unique values
      - Show field: Name (with presence)
      - **Note**: make sure to note the field name (all text after _Field=_ in URL)
    - {Activity Name}
      - Choice
      - Description: Has been completed?
      - Type each choice on a separate line:
        - Yes
        - No
      - Display choices using Drop-Down Menu
      - Allow 'Fill-in' choices: No
      - Default value: Choice: No
      - **Note**: create as many {Activity Name} columns using this format
    - Trainee Year
      - Calculated
      - Formula: `=TEXT(Title,"yyyy")`
    - Trainee Month
      - Calculated
      - Formula: `=TEXT(Title,"mmmm")`
  - Apply formatting to each {Activity Name} row (Green for Yes; Red for No)
- Create a MS Form (**not** a quiz; will need one for **each** {Activity name} activity)
  - One question:
    - "I certify that I have completed my {Activity Name} activity.
      - Answer Option(s): "Yes"
      - Required
  - Set to only one response per person
- Create a MS Flow (Power Automate) Part 01:
  - Add Trigger:
    - When a new response is submitted (MS Form)
      - Form ID: ID from MS Form URL
- Create a MS Flow (Power Automate) Part 02:
  - Add an Action:
    - Apply to each
      - Select an output from previous steps: _List of responses_: `triggerOutputs()?[‘body/value’]`
      - **Note**: this _action_ is the parent of **all** remaining actions to follow...
  - Add an Action:
    - Get response details
      - Form ID: ID from MS Form URL
      - Response ID: _List of responses_: `items(‘Apply_to_each’)?[‘resourceData/responseId’]`
  - Add an Action:
    - Get items (**not** "Get item")
      - Site Address: ...
      - List Name: ...
      - Filter Query (click "Show advanced options")
        - `Trainee_x0020_Name/EMail eq 'Responders Email'` (Responders Email should be a choice in the drop-down for this field)
- Create a MS Flow (Power Automate) Part 03:
  - Add an Action:
    - Condition
      - First field (expression): `empty(outputs('Get_items')?['body/value'])`
      - Second field: `is equal to`
      - Third field (expression): `false`
- Create a MS Flow (Power Automate) Part 04A (**IF YES**):
  - Add an Action:
    - Apply to each
      - Select an output from previous steps: `value`
  - Add an Action (**as a child**)
    - Apply to each
      - Select an output from previous steps: `value`
  - Add an Action (**as a child**)
    - Update item (Sharepoint)
      - Site Address: ...
      - List Name: ...
      - Id: `ID`
      - Title: `Title`
      - Trainee Claims: `Trainee Claims`
      - {Activity Name}: add "Yes" **only** for the activity we are collecting the MS Form data from; Leave the remaining fields blank
- Create a MS Flow (Power Automate) Part 04B (**IF NO**):
  - Add an Action
    - Create item (Sharepoint)
      - Site Address: ...
      - List Name: ...
      - Title: `Title`
      - Trainee Claims: `Trainee Claims`
      - {Activity Name}: add "Yes" **only** for the activity we are collecting the MS Form data from; Leave the remaining fields blank

## For a Survey that uses the "Average" functionality

- MS Lists
  - Any field that will need to be averaged **needs** to be changed to _Number_ **not** _Choice_.
  - For formatting I used:
    - If {columnValue} is greater than 3, then green
    - If {columnValue} is equal to 3, then yellow
    - If {columnValue} is less than 3, then red
  - Select the column drop-down and at the bottom there should be an option to select "Count" **or** "Average" (as applicable)
- MS Power Automate
  - Need to use `outputs('Get_response_details')?['body/FIELD_ID']` to select the applicable field, but we also need to wrap that with `int()` in order to convert it to numeric format over string-literal.


## Create a Power Automate for Multi-Select Data
When trying to send data from a MS Form multi-select, it appears as if MS List does **not** know enough to break-down the data especially for a *Choices* column. Based on research, using a *Choices* column for multi-select is not currently supported functionality. Given this information, you must output it to a single **or** multi-line text field, however when doing that the data comes across as JSON-like format with parenthesis, brackets, and quotes. So you need to handle it accordingly with the formula below:
- [Resource One - YouTube](https://www.youtube.com/watch?v=tMLLq4h59Mw)
- In the table field for the column enter the following 'fx' equation (**note:** swap out the ID):

```jsx
join(array(json(outputs('Get_response_details')?['body/rd57688520b38480a92d57e8bbfcb9024'])), ',')
```
This formula converts the output into JSON, then the JSON is converted to an array. After that, the `join()` function outputs each value of the array with the predetermined delimeter which, in this case, is a comma.

---
# JSON 101
---
- JSON consists of key/value pairs
  - Keys **must** be strings
  - Values **must** be a valid JSON data type

## Data Types
- string: "name" : "Mike"
- number: "age" : 30
- object: {"employee" : {"name": "Mike", "age": 30}}
- array: {"employees" : ["Mike", "Alyssa", "Dani"]}
- boolean: "sale" : true
- null: "car" : null

## Misc Information
- JSON String: `'{"name": "Mike", "age": 30, "car": null}'`
- JSON Object Literal: `{"name": "Mike", "age": 30, "car": null}`
- JSON **cannot** be an object. JSON is a string format