from RemoveBase import RemoveBlocked

if __name__ == "__main__":
    rmBlocked = RemoveBlocked(log_name="block_coi_removed_may_26_2020.txt",
                              category="User talk pages with conflict of interest notices",
                              target="[[Category:User talk pages with conflict of interest notices|{{PAGENAME}}]]",
                              brfa="TheSandBot 10")
    try:
        rmBlocked.run()
    except KeyboardInterrupt:
        print("\n")
