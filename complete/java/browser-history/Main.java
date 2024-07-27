/*
 * Name: Browser History
 */

import java.util.*;

class BrowserHistory {
    private List<String> history; 
    private int currentIndex;

    public BrowserHistory(String homepage) {
        this.history = new ArrayList<String>();
        this.history.add(homepage);
        this.currentIndex = 0;
    }

    public void visit(String url) {
        this.history = this.history.subList(0, currentIndex + 1);
        this.history.add(url);
        this.currentIndex = this.history.size() - 1;
        return;
    }
        
    public String back(int steps) {
        if (this.currentIndex - steps <= 0)
            this.currentIndex = 0;
        else
            this.currentIndex = this.currentIndex - steps;
        return currentURL();
    }
            
    public String forward(int steps) {
        if (this.currentIndex + steps >= this.history.size())
            this.currentIndex = this.history.size() - 1;
        else
            this.currentIndex = this.currentIndex + steps;
        return currentURL();
    }

    private String currentURL() {
        String url = this.history.get(this.currentIndex);
        System.out.println("HTTPS:// " + url);
        return url;
    }
}

class Main {
    public static void main(String[] args) {
        BrowserHistory bh = new BrowserHistory("leetcode.com");
        bh.visit("google.com");
        bh.visit("facebook.com");
        bh.visit("youtube.com");
        bh.back(1);
        bh.back(1);
        bh.forward(1);
        bh.visit("linkedin.com");
        bh.forward(2);
        bh.back(2);
        bh.back(7);
    }
}