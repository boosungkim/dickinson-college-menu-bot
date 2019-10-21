package Menu;

public class DiningMenu {
	public DiningMenu() {
		GrabbingMenu.scanMenu();
		
	}
	
	
	public String[] divideLines(int location, int meal) {
		String[] menuList = GrabbingMenu.getMenu(location)[meal].split("(?=Soup:)|(?=Entree:)|(?=Grain:)"
				+ "|(?=Wrap:)|(?=Grill:)|(?=Side:)");
		return menuList;
	}
	
	
	public String formatMenu() {
		String tempMB = "";
		String tempML = "";
		String tempMD = "";
		
		for(int ln = 0; ln < divideLines(GrabbingMenu.DINING, GrabbingMenu.FIRST).length; ln++) {
			tempMB = tempMB + divideLines(GrabbingMenu.DINING, GrabbingMenu.FIRST)[ln] + "\n";
		}
		formatChar(tempMB);
		
		for(int ln = 0; ln < divideLines(GrabbingMenu.DINING, GrabbingMenu.SECOND).length; ln++) {
			tempML = tempML + divideLines(GrabbingMenu.DINING, GrabbingMenu.SECOND)[ln] + "\n";
		}
		formatChar(tempML);
		
		for(int ln = 0; ln < divideLines(GrabbingMenu.DINING, GrabbingMenu.THIRD).length; ln++) {
			tempMD = tempMD + divideLines(GrabbingMenu.DINING, GrabbingMenu.THIRD)[ln] + "\n";
		}
		formatChar(tempMD);
		
		String diningEmail = "Today's Dining Hall Menu is:\n"
				+ "---Breakfast---\n"
				+ tempMB
				+ "---Lunch---\n"
				+ tempML
				+ "---Dinner---\n"
				+ tempMD
				+ "\n\n";
		return diningEmail;
	}
	
	
	public void formatChar(String line) {
		line = line.replaceAll(":", ": ");
		line = line.replaceAll("w/", "with ");
		line = line.replaceAll("&", "and");
	}
}
