# cl3ver

A python3 wrapper for the cleverbot API


## API KEY

[To use the Cleverbot API, you will need to register for a key!](http://www.cleverbot.com/api/)


## INSTALLATION

    pip install cl3ver


## USAGE

```
>>> import cl3ver
>>> CB = cl3ver.Cl3ver('YOUR_API_KEY')
>>> CB.say("what's up cleverbot?")
'What are you doing tonight?'
```

Pass an optional name (or ID) to maintain the state of different conversations:

```
>>> CB.say('nice to meet you cleverbot!', 'jane')
'Me too.'
>>> CB.say('how is your day going?', 'jane')
'Pretty good, how about your day.'
>>> CB.say('привет', 'vlad')
'Ты кто?'
```
