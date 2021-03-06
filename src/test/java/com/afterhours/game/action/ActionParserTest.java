package com.afterhours.game.action;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ActionParserTest {
    ActionParser testObj = new ActionParser();

    @Test
    void parseActionGibberish() {
        Action action = testObj.parseAction("?asdnmaf");
        assertEquals(action.name(), "GIBBERISH");
    }

    @Test
    void parseActionMove() {
        Action action = testObj.parseAction("move north");
        assertEquals(action.name(), "MOVE");
    }

    @Test
    void parseActionGo() {
        Action action = testObj.parseAction("go north");
        assertEquals(action.name(), "MOVE");
    }

    @Test
    void parseActionNorth() {
        Action action = testObj.parseAction("north");
        assertEquals(action.name(), "MOVE");
    }

    @Test
    void parseActionNorthSingleLetter() {
        Action action = testObj.parseAction("n");
        assertEquals(action.name(), "MOVE");
    }

    @Test
    void parseActionTalk() {
        Action action = testObj.parseAction("talk to beth");
        assertEquals(action.name(), "TALK");
    }

    @Test
    void parseActionSay() {
        Action action = testObj.parseAction("say hi to beth");
        assertEquals(action.name(), "TALK");
    }

    @Test
    void parseActionLook() {
        Action action = testObj.parseAction("look north");
        assertEquals(action.name(), "LOOK");
    }

    @Test
    void parseActionExamine() {
        Action action = testObj.parseAction("examine badge");
        assertEquals(action.name(), "LOOK");
    }

    @Test
    void parseActionClose() {
        Action action = testObj.parseAction("close");
        assertEquals(action.name(), "CLOSE");
    }

    @Test
    void parseActionInventory() {
        Action action = testObj.parseAction("inventory");
        assertEquals(action.name(), "INVENTORY");
    }

    @Test
    void parseActionI() {
        Action action = testObj.parseAction("i");
        assertEquals(action.name(), "INVENTORY");
    }

    @Test
    void parseActionQuit() {
        Action action = testObj.parseAction("quit");
        assertEquals(action.name(), "QUIT");
    }
}
