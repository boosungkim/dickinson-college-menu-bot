import java.util.*;

public class testing{
    public static void main(String[] args){
        String html = "<html><head><title>First parse</title></head>"
  + "<body><p>Parsed HTML into a doc.</p></body></html>";
Document doc = Jsoup.parse(html);
    }
}