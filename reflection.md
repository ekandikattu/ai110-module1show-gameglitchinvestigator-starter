# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

1. The hint given is the opposite of what it should be. For example, the hint would be higher if the guess was higher than the actual number, and vice versa.
2. The "New Game" button does not work. It will not clear guesses from the previous game (or update the score back to 0).
3. The difficulty levels are switched around. The "Hard" difficulty should be switched with the "Normal" difficulty.
4. Updating the difficulty level does not change the secret value or the number of attempts (it always stays on Normal difficulty settings).
5. The number of "Attempts Left" displayed is 1 less than the actual number of attempts at the start of the game. The first attempt does not change the display, but every other attempt changes the display. (Ex. On Normal mode, you can take 7 attempts by clicking guess 8 times, where the first guess will not register).
6. The debug history records guesses with an offset of 1, such that the on 2nd guess, the first will be added to the history list, and so on until the n-1 is added on the nth guess. 
7. The Final Score calculation does not follow any logical pattern based on the number of guesses used before hitting the target.
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

1. I used Copilot for this project.

2. Correct Example: When I asked Copilot about where the code logic was for the inverted hint suggestion error, it correctly identified the conditional logic being inverted, resulting in the opposite print statements for hints following each guess. After I asked it to fix that conditional logic block and create a pytest test case to show it was fixed, it performed both tasks correctly and the pytest case passed successfully. When I inspected the hints myself, the feature was working as intended.

3. Incorrect Example: I asked copilot to fix multiple bugs at once affecting the secret number generation, but it did not fix one of the bugs due to my prompting being more general and not specific enough. I verified it did not fix the bug by testing the app myself and going over the agent solution code to find the other fixes but not the one I was looking for. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

1. I decided when a bug was fixed by looking through the agent solution to the problem (and using ask to clarify how it did it if I was confused) and also playing with the app to ensure that the feature (even if it did pass the pytest) was working as intended. 

2. One test I ran was using the show hint feature and checking if it was giving the right hint on each guess. 
3. Copilot helped design all pytests and go over the solutions to the problems I gave, which gave me a clear understanding of what it did and why the pytest case passed. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

1. The secret number kept changing in the original app when u interact with anything in the app because there was code logic to rerun the session state. 
2. Streamlit session state is like a save of what has happened in the game. It records what is happening in the game, and a rerun refreshes that state to its original form (the unplayed game). 
3. I worked with Copilot to refresh game state only at controlled times and store it, which ensured that progress would not be lost and changes would be updated accordingly. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

1. One habit I want to reuse in future labs is test-driven development, which would help to ensure changes I make do what I intend for them to do in a quantifiable, measurable way to others. 
2. One thing I would do differently would be using #codebase to go over the different parts of the app in each file to better understand the inner workings BEFORE I started looking for fixes. 
3. This project has solidified my understanding of using AI to debug and problem solve on code, and also taught me more about how to speed up my understanding of the codebase and writing regression tests on my fixes.
