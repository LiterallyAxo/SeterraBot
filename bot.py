import asyncio
import logging
import sys
from colorama import Fore, Style, init
from playwright.async_api import async_playwright

init(autoreset=True)

class SeterraBot:
    def __init__(self, delay: int = 0):
        self.delay = delay
        self.click_count = 0
        self.last_state_name = None
        self.browser = None

        logging.basicConfig(
            level=logging.INFO,
            format=f"{Fore.GREEN}[%(asctime)s]{Style.RESET_ALL} {Fore.CYAN}%(levelname)s{Style.RESET_ALL}: %(message)s",
            datefmt="%H:%M:%S"
        )

    async def start(self):
        try:
            async with async_playwright() as p:
                self.browser = await p.chromium.launch(headless=False)
                page = await self.browser.new_page()
                await self.load_page(page)
                await self.monitor_instructions(page)
        except Exception as e:
            logging.error(f"Unexpected error during execution: {str(e)}")
        finally:
            if self.browser:
                await self.browser.close()

    async def load_page(self, page):
        try:
            logging.info("Navigating to GeoGuessr page...")
            await page.goto("https://www.geoguessr.com/vgp/3003", wait_until="domcontentloaded")
            await self.scroll_to_main_area(page)
        except Exception as e:
            logging.error(f"Failed to load page or scroll to main area: {str(e)}")

    async def scroll_to_main_area(self, page):
        try:
            main_area = await page.wait_for_selector("[class^='seterra_main__']", timeout=5000)
            if main_area:
                await main_area.scroll_into_view_if_needed()
                await page.evaluate("window.scrollBy(0, 350)")
                logging.info("Scrolled to the main map area with an extra 350px adjustment.")
        except Exception as e:
            logging.error(f"Failed to scroll to the main map area: {str(e)}")

    async def monitor_instructions(self, page):
        logging.info("Monitoring the page for state instructions...")
        while True:
            try:
                if not self.browser.is_connected():
                    logging.info("Browser window closed, stopping the program.")
                    break

                instruction = await page.query_selector("text=Click on")
                if instruction:
                    instruction_text = await instruction.text_content()
                    if "Click on" in instruction_text:
                        state_name = instruction_text.split("Click on ")[1].strip()
                        await self.click_state(page, state_name)
                await asyncio.sleep(self.delay)
            except Exception as e:
                logging.error(f"Error while monitoring instructions: {str(e)}")
                break

    async def click_state(self, page, state_name: str):
        try:
            if state_name != self.last_state_name:
                logging.info(f"Instruction detected: Click on {Fore.YELLOW}{state_name}{Style.RESET_ALL}")

                game_area_selector = "[class^='game-area_gameArea__']"
                state_selector = f"{game_area_selector} #AREA_{state_name.upper().replace(' ', '')} [data-type='hitbox-area']"
                logging.info(f"Looking for element with selector: {state_selector}")

                element = await page.query_selector(state_selector)

                if element:
                    box = await element.bounding_box()
                    if box:
                        x = box['x'] + box['width'] / 2
                        y = box['y'] + box['height'] / 2
                        if state_name.upper() == 'LOUISIANA':
                            x -= 20
                        if state_name.upper() == 'MICHIGAN':
                            x += 20

                        logging.info(f"Clicking on the center of {Fore.YELLOW}{state_name}{Style.RESET_ALL} at ({x:.2f}, {y:.2f})")
                        await page.mouse.click(x, y)
                        self.click_count += 1
                        self.last_state_name = state_name

                        if self.click_count >= 50:
                            logging.info("Reached 50 successful clicks, stopping the program.")
                            await asyncio.sleep(30)
                            await self.browser.close()
        except Exception as e:
            logging.error(f"Failed to click on state {state_name}: {str(e)}")

if __name__ == "__main__":
    delay = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    bot = SeterraBot(delay)
    asyncio.run(bot.start())
