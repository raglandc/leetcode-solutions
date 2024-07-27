/*
    browser-history-ll
*/

class UrlHistoryNode {
    String url;
    UrlHistoryNode prev;
    UrlHistoryNode next;

    UrlHistoryNode(String url) {
        this.url = url;
        this.prev = null;
        this.next = null;
    }
}

class BrowserHistory {
    UrlHistoryNode current;

    BrowserHistory(String homepage) {
        this.current = new UrlHistoryNode(homepage);
    }

    public void visit(String url) {
        System.out.println("Visiting " + url + "...");
        UrlHistoryNode currentNext = this.current.next;
        if (currentNext != null) currentNext.prev = null;
        UrlHistoryNode newUrl = new UrlHistoryNode(url);
        newUrl.prev = this.current;
        this.current.next = newUrl;
        this.current = newUrl;
        return;
    }

    public String back(int steps) {
        while (steps > 0 && this.current.prev != null) {
            this.current = this.current.prev;
            steps--;
        }
        System.out.println("http://wwww." + this.current.url);
        return this.current.url;
    }
        
    public String forward(int steps) {
        while (steps > 0 && this.current.next != null) {
            this.current = this.current.next;
            steps--;
        }
        System.out.println("http://wwww." + this.current.url);
        return this.current.url;
    }

}

public class Main {
    public static void main(String[] args) {
        System.out.println("Linked List Browser History");
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
