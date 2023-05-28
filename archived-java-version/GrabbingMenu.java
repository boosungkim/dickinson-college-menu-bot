// package Menu;

import java.io.IOException;
import java.util.Arrays;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class GrabbingMenu {
	public static String[] allMenu = new String[7];
	public static Elements menuItems;
	
	public static final int FIRST = 0;
	public static final int SECOND = 1;
	public static final int THIRD = 2;
	
	public static final int DINING = 10;
	public static final int UNION = 11;
	public static final int KOVE = 12;
	
	
	public static void scanMenu() {
		Link today = new Link();
		try {
			Document doc = Jsoup.connect(today.getLink()).get();
			menuItems = doc.getElementsByClass("menuItems");
			findItems(menuItems);
			} catch (IOException e) {
				e.printStackTrace();
			}
	}
	
	
	public static void findItems(Elements e) {
		int tempI = 0;
		for(Element el : e) {
			allMenu[tempI]= el.text();
			tempI++;
		}
	}
	
	
	public static String[] getMenu(int place) {
		if(place == DINING) {
			return Arrays.copyOfRange(allMenu, 0, 3);
		}else if(place == UNION) {
			return Arrays.copyOfRange(allMenu, 3, 5);
		}else if(place == KOVE) {
			return Arrays.copyOfRange(allMenu, 5, 7);
		}else {
			return null;
		}
	}
}
