package com.afterhours.game.player;

import com.afterhours.game.inventory.Inventory;
import com.afterhours.game.inventory.Item;
import com.afterhours.game.inventory.ItemParser;
import com.afterhours.game.inventory.ItemUtils;
import com.afterhours.game.location.Location;

public class Player {
    private Inventory inventory;
    private Location location;
    private ItemParser itemParser;

    public Player() {
        inventory = new Inventory(new Item[]{Item.BADGE, Item.NIGHTSTICK});
        location = Location.LOBBY;
        itemParser = new ItemParser();
    }

    public Location getLocation() {
        return location;
    }

    public Inventory getInventory() {
        return inventory;
    }

    public String printInventory() {
        StringBuilder output = new StringBuilder();
        for (Item item : inventory.getInventoryContents()) {
            output.append("a " + item.toString().toLowerCase() + ", ");
        }

        return "In your possessions, you have " + ItemUtils.generateListOfItems(inventory.getInventoryContents()) + "and the lint in your pockets.";
    }

    public String look(int x, int y) {
        Location currentLocation = location;
        int newX = location.getX() + x;
        int newY = location.getY() + y;
        for (Location location : Location.values()) {
            if (location.getX() == newX && location.getY() == newY) {
                return location.getOutsideDescription();
            }
        }
        return currentLocation.getDescription();
    }

    public String move(int x, int y) {
        Location currentLocation = location;
        int newX = location.getX() + x;
        int newY = location.getY() + y;
        for (Location location : Location.values()) {
            if (location.getX() == newX && location.getY() == newY) {
                this.location = location;
                return location.getDescription();
            }
        }
        if (currentLocation == location) {
            return "You can't go that way.";
        }
        return "Pardon?";
    }

    public String pickup(String itemString) {
        Item item = itemParser.parseItem(itemString);
        if (item.equals(Item.NOT_FOUND)) {
            return "failure, not found";
        } else if (!item.isTakeable()) {
            return "failure, not takeable";
        } else if(!location.getItemsList().contains(item)) {
            return "failure, not reachable";
        }
        inventory.addToInventory(item);
        location.takeItem(item);
        return "success";
    }

    public String drop(String itemString) {
        Item item = itemParser.parseItem(itemString);
        if (item.equals(Item.NOT_FOUND)) {
            return "failure, not found";
        } else if(!inventory.getInventoryContents().contains(item)) {
            return "failure, not possessed";
        }
        inventory.removeFromInventory(item);
        location.dropItem(item);
        return "success,dropped";
    }

    private String verifyItemOpenable(Item item) {
        if (item.equals(Item.NOT_FOUND)) {
            return "failure, not found";
        } else if (!Item.isOpenable(item)) {
            return "failure, not openable";
        } else if(!getLocation().getItemsList().contains(item)) {
            return "failure, not reachable";
        }
        return "success," + (item.isOpen() ? "open" : "closed");
    }

    public String open(String itemString) {
        Item item = itemParser.parseItem(itemString);
        String status = verifyItemOpenable(item);
        if (status.equals("success,closed")) {
            item.open();
        }
        return status;
    }

    public String close(String itemString) {
        Item item = itemParser.parseItem(itemString);
        String status = verifyItemOpenable(item);
        if (status.equals("success,open")) {
            item.close();
        }
        return status;
    }
}
