---
categories: ["Fuel & Tuning"]
tags: [EFI, Holley Sniper, Tuning]
title: "Holley Sniper EFI"
date: 2017-10-30 12:00:00 +0000
---

![Holley Sniper EFI](/assets/img/posts/SniperEFI.png){: .no-lightbox style="display: block; margin: 0 auto; max-width: 100%; border-radius: 8px;"}

The 1967 Camaro was born with a single barrel carburetor and inevitably rebuild with a [Holley 600CFM Double Pumper with Mechanical Secondaries](/posts/carburetor/). That carburetor actually worked pretty well, but not only was it difficult to keep in tune as a daily driver in different areas and rapidly changing weather conditions, it never really fit the build. **Turbo Camaro** has always been about custom upgrades and improvements over stock. While not saying a carburetor doesn't have it's place, it just isn't a modern choice for a car peeling away from stock.

Dozens of hours were spent researching available Electronic Fuel Injection (EFI) options. With most popular options starting at $999US you can get in the market easily but once you commit to a specific system or brand, you are stuck with it unless you intend to buy multiple systems. With FAST, Edelbrock, Holley and FiTech competing with each other, it opens the door for very similar products, making the choice that much more difficult. For a basic recount of the standings, FAST was early to the game but has since fallen short. Edelbrock also released a decent system but performance results were sub par. Holley had several high priced units with success but the lower priced Sniper unit was new and unproven. FiTech had one of the first budget priced quality units to perform well, but doesn't match the newer Holley Sniper features/specs. Most specifically the injector ratings, laptop software and AFR grid sizes. At the time of consideration, early reports indicated users had improved learning and performance with the Holley Sniper. One of the biggest considerations is the name brand. Normally we don't care much for brands, but when it's **Holley vs. FiTech** it's a big deal. Which brand has been in the game longer, and which one will still be there, supporting products in 10 years?

![EFI System Pro](/assets/img/posts/efisystempro_final_2_stacked.png){: .no-lightbox style="display: block; margin: 0 auto; max-width: 60%;"}

We sourced our Sniper Master Kit from [EFISystemPro.com](http://www.efisystempro.com/). So we went with the [Holley Sniper EFI Master Kit](https://www.efisystempro.com/sniper/sniper-efi-black){:target="_blank"} from [EFI System Pro](https://www.efisystempro.com/){:target="_blank"}. It won't seem like a big deal 5 years from now, but EFI System Pro actually had stock on the Sniper when nobody else did, and the price couldn't be beat. Their customer service helped me realize I'd need an extra EFI fuel return line and a [Can to USB dongle](https://www.efisystempro.com/can-usb-dongle-558-443){:target="_blank"} cable for live tuning the fuel and boost tables. That being said, upon release, the Holley Sniper system didn't support a blow through turbocharger as the base software tables didn't include presets for boost. With the addition of the Holley Tuning Software, you can use the dongle cable to get the job done. Beyond that, the Sniper can run up to 650 horse power. Technically the built in injectors can handle a lot more, but internal restrictions apparently don't keep up well much beyond the 650 point.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/9nSIgjn9NZQ?feature=player_embedded" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
</div>

With the Sniper unboxed, it was time to do some comparisons against the trusty Holley 600CFM. The inline 6 has limited space on the passenger side of the intake as it sits almost up against the valve cover. You can see in the image below that, unfortunately, the Sniper system puts the linkage out an additional ½" or so.

![Sniper vs Carb Top View](/assets/img/posts/SniperCarbTop.jpg){: .no-lightbox style="display: block; margin: 0 auto; max-width: 100%; border-radius: 8px;"}

Of course a consideration for anyone is height vs. hood clearance. Various sources say the Holley Sniper is about the same height as a typical carburetor, and they're right. Our comparison below to the real deal proved just that.

![Sniper vs Carb Side View](/assets/img/posts/SniperCarbSide.jpg){: .no-lightbox style="display: block; margin: 0 auto; max-width: 100%; border-radius: 8px;"}

A solid weekend later, the Holley Sniper EFI system and Master Kit was installed in the camaro. Rather than reading the outcome, take a look at our how-to video:

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/cRLbxH4TMik?feature=player_embedded" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
</div>

With the Holley Sniper EFI running smooth, we really want to set it up to control timing but not all options are equal in desirability and some simply aren't compatible with our Inline 6.

**Option 1: [Holley Dual Sync Distributor](https://www.efisystempro.com/index.php?route=product/search&search=holley%20dual%20sync&description=true){:target="_blank"} (DSD) with hall effect trigger** and a stand alone coil. This is easily the best route if you want a hassle free install that just works. Most forums and parts suppliers will suggest you go with a DSD as it's hall effect trigger is immune to common radio frequency interference that plagues its magnetic brethren. Unfortunately Holley has yet to craft a DSD for the Chevy 250.

**Option 2: MSD Distributor with magnetic trigger**, stand alone coil and [MSD Rotor Phasing Kit](https://www.efisystempro.com/msd-rotor-phasing-kit-84211){:target="_blank"}. This option would probably get the job done, but considering the cost of all the parts required, and to end up with a magnetic pickup, it just doesn't seem like the best bang for buck. If you already had this distributor then obviously you should lock it out and give it a whirl, but I wouldn't want to buy this for a new build if a DSD was available.

**Option 3: Large Cap GM HEI Distributor with magnetic trigger** and built in coil, manually phased. This is obviously the cheapest, but requires taking the road less traveled. By "less traveled" I mean someone's been on it a couple times and the footprints are faint at best. Very little information exists on the "best" way to setup a coil in large cap HEI distributor for timing control, but it has been done by at least a couple people and seems to work well for them. This would obviously be the cheapest method but requires some ingenuity.

For more information about wiring the above ignition options I recommend checking out [Demystifying Holley Terminator and Sniper Ignition Hookup](https://www.efisystempro.com/efi-pro-hangout/demystifying-holley-terminator-sniper-ignition-wiring){:target="_blank"} or referencing the official [Holley Forums](https://forums.holley.com/){:target="_blank"}.

For a complete video tutorial covering all aspects of electronic timing control with a GM HEI Distributor and the Holley Sniper EFI System take a look at our video:

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/L9xRJKmaPwA?feature=player_embedded" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
</div>

### Installation Steps Recap:

1. Remove the distributor and confirm you are using a smiliar 4 pin module version. Ours was sourced off eBay 7 years ago. Here is a [similar distributor](https://www.ebay.ca/itm/352082630332){:target="_blank"}.
   
   ![GM HEI Timing](/assets/img/posts/GMHEITiming1.jpg_large.jpg){: .no-lightbox style="display: block; margin: 10px auto; max-width: 300px; border-radius: 8px;"}

2. If so, **lockout the mechanical advance**. You can weld it, secure it with a screw or make/buy a distributor lockout plate.
3. Secure the vacuum advance rod or reluctor adjustment tab. For simplicity we used a [Speedway HEI Manual adjustment knob](https://www.youtube.com/redirect?q=https%3A%2F%2Fwww.speedwaymotors.com%2FHEI-External-Timing-Adjustment-Knob%2C1689.html&event=video_description&v=L9xRJKmaPwA&redir_token=O8-e9_Ps2GkK9TzQxZ1dUAYJlBZ8MTUxNzc2Nzc5NkAxNTE3NjgxMzk2){:target="_blank"}, which allowed for easy rotor phasing later on.
4. Set your engine timing to your desired reference angle, 10° higher than the maximum timing you'd want your motor to see. If you want 36° at wide open throttle, make your reference angle between 46-60° BTDC on the compression stroke. **For the video and these instructions, your timing is set to 46°**.
5. Fully seat your distributor with the housing in the desired position and your rotor pointed toward the #1 Spark plug terminal on your distributor cap.
6. Mark the edge of your distributor housing with the location of the brass contact of your #1 Spark Plug terminal.
7. Turn the distributor housing to line up the closest reluctor magnet with the pickup.
8. Secure the distributor.
9. Use the vacuum advance knob or rod to adjust the reluctor to ensure the rotor is pointing near the most counter-clockwise point that you marked on the housing. This will ensure when your engine drops from **46°** to 36° it will be partially in front of the brass terminal.
10. Once you're happy with the phasing, check it by moving to your engine timing to it's mid range. If you crank at 15° and go wide open at 36° then move your engine to 20°. At 20° your rotor should be close to perfectly centered in front of the brass terminal of your #1 spark plug.
11. Hookup your magnetic pickup wires to the green/purple crank trigger wires of your Sniper EFI System. We used this [MSD HEI Module Bypass Cable](https://www.speedwaymotors.com/MSD-8861-GM-HEI-Module-Bypass-Cable,64076.html){:target="_blank"} wich allowed us to use the connector on the Sniper harness and plug right into the magnetic pickup connector.
12. If you're using the Holley Coil Driver, hookup its grey wire to the Tach terminal on the distributor, or to where the module plugged in on terminal "C".
13. The Holley Coil Driver requires a ground connection, white wire to the Sniper main harness and a pink accessory 12v power connection. We spliced the pink wire into the pink wire supplied to the main harness of the Sniper EFI system and it worked perfectly.
14. Pull the fuel relay or prevent fuel delivery somehow.
    
    ![Reluctor Lineup](/assets/img/posts/ReluctorLineup.jpg_large.jpg){: .no-lightbox style="display: block; margin: 10px auto; max-width: 100%; border-radius: 8px;"}

15. Open your ECU config in the Holley Sniper EFI software (via CAN/USB dongle or manually via SD Card).
16. Under Engine Parameters, Set your Ignition Type to "Magnetic", Reference Angle to "**46°**", Minimum Signal Voltage to "0.65" and Filtering to "High". Take the opportunity to ensure the Base Timing Table is at least in the right ballpark for your engine. Save the config.
17. Upload the new/saved config file to your Sniper ECU.
18. Set Static Timing Check to 15° and turn the key. With a timing light your engine should crank near 15°. If it cranks within a few degrees, make the small adjustment to your distributor housing to set it at 15°. Try cranking again to ensure it is now locked at 15° during the static timing check.
19. Re-install the fuel relay or activate your fuel system.
20. Set the Static Timing Check to 15° again, and start the engine. With the engine running, ensure it sits at 15°. Again, if it's very close but could be better, make the small couple degree adjustment.
21. Increase the engine RPM to verify the static timing holds. It won't, so in the Ignition Settings (handheld), try increasing the Inductive Delay to "0.100" and power cycle the engine. Re-enable the Static Timing check of 15° and increase the RPM again. Our vehicle's timing moved to approximately 16° at 3500RPM, which is an acceptable amount of movement. You may be able to fine tune the Inductive Delay to get it even better.
22. Clear the static timing and take it for a drive. If you've been rapidly cranking and starting/stopping the engine, you may want to give it a good run to charge up the battery.

Obviously these instructions, and the video couldn't cover every little aspect of this procedure but being confident in the installation, we'd be happy to help however we can. **Turbo Camaro** is running better than ever and I'm happy to say we can probably make it even better. We still have to tune the boost and fuel tables for maximum performance...

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/ou_0ax39b1M?feature=player_embedded" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
</div>

And now that we're actually setup properly to run boost on our Sniper, we can really begin to drive it and let the system learn the engine. Just to throw another twist on things, I really wanted to install a **progressive link** on the Sniper. I was a big fan of the *Mechanical Secondaries* feel of our old Holley 600, so a new linkage for the Sniper would give use the best of both fuel systems. For just a few bucks, the car seems to be more efficient and has a much smoother pedal feel. Take a look below.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; border-radius: 8px;">
  <iframe src="https://www.youtube.com/embed/YFDibprdfW4?feature=player_embedded" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" allowfullscreen></iframe>
</div>

Interested in checking out the Turbo Camaro Sniper EFI configuration File? [Download it here](http://www.mediafire.com/file/owck90pd0nzr1wg/TC-JUL2018-5.sniper/file){:target="_blank"}
