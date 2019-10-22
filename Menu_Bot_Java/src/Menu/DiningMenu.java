package Menu;

public class DiningMenu {
	public DiningMenu() {
		GrabbingMenu.scanMenu();
	}
	
	
	public String[] divideLines(int location, int meal) {
		String[] menuList = GrabbingMenu.getMenu(location)[meal].split("(?=Soup:)|(?=Entree:)|(?=Grain:)"
				+ "|(?=Wrap:)|(?=Grill:)|(?=Side:)|(?=Lunch Special:)|(?=Dinner Special:)|(?=Nightly Special:)");
		return menuList;
	}
	
	
	public String formatMenu() {
		String diningEmail = "Today's Dining Hall Menu is:\n"
				+ "---Breakfast---\n"
				+ formatSection("", GrabbingMenu.DINING, GrabbingMenu.FIRST)
				+ "---Lunch---\n"
				+ formatSection("", GrabbingMenu.DINING, GrabbingMenu.SECOND)
				+ "---Dinner---\n"
				+ formatSection("", GrabbingMenu.DINING, GrabbingMenu.THIRD)
				+ "\n\n";
		return diningEmail;
	}
	
	
	public String formatSection(String line, int place, int meal) {
		for(int ln = 0; ln < divideLines(place, meal).length; ln++) {
			line = line + divideLines(place, meal)[ln] + "\n";
		}
		line = line.replaceAll(":", ": ");
		line = line.replaceAll("w/", "with ");
		line = line.replaceAll("&", "and");
		return line;
	}
}
