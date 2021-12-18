import json
import re
import string

from pydantic.dataclasses import dataclass
from datetime import datetime

# Write your awesome code here
from collections import defaultdict


class EasyRiderBusCompany:
    def __init__(self, bus_data_json):
        self.bus_data_json = bus_data_json
        self.bus_data = json.loads(self.bus_data_json)
        self.bus_id_errors = 0
        self.stop_id_errors = 0
        self.stop_name_errors = 0
        self.next_stop_errors = 0
        self.stop_type_errors = 0
        self.a_time_errors = 0
        self.bus_routes = []

    def load_and_verify_database(self):
        for bus in self.bus_data:
            self.validate_bus_id(bus)
            self.validate_stop_id(bus)
            self.validate_stop_name(bus)
            self.validate_stop_type(bus)
            self.validate_next_stop(bus)
            self.validate_a_time(bus)
            self.bus_routes.append(EasyRiderBusData(**bus))

    def get_different_types_of_stops(self):
        # Get the unique buses first
        buses = set(route.bus_id for route in self.bus_routes)
        start_stops = []
        stops = defaultdict(int)
        finish_stops = []
        on_demand_stops = []
        # Check if each of these buses have both a single start stop and a finish stop
        for bus in buses:
            # Get the count of start stops and finish stops for the bus
            routes = [route for route in self.bus_routes if route.bus_id == bus]
            start_count = 0
            finish_count = 0
            on_demand_count = 0
            for route in routes:
                if route.stop_type == "O":
                    on_demand_stops.append(route.stop_name)
                    on_demand_count += 1
                if route.stop_type == "S":
                    start_stops.append(route.stop_name)
                    start_count += 1
                if route.stop_type == "F":
                    finish_stops.append(route.stop_name)
                    finish_count += 1
                if start_count > 1 or finish_count > 1:
                    print(f"There are more than one start stop or end stop for the line: {bus}")
                    exit()
                stops[route.stop_name] += 1
            if start_count == 0 or finish_count == 0:
                print(f"There is no start stop or end stop for the line: {bus}")
                exit()
        transfer_stops = set([name for name, count in stops.items() if stops[name] > 1])
        return set(start_stops), transfer_stops, set(finish_stops), set(on_demand_stops)

    def verify_print_info_about_routes(self):
        start_stops, transfer_stops, finish_stops, _ = self.get_different_types_of_stops()
        total_start_count = len(start_stops)
        transfer_stops_count = len(transfer_stops)
        total_finish_count = len(finish_stops)
        # print(f"Start stops: {total_start_count} {sorted(set(start_stops))}")
        # print(f"Transfer stops: {transfer_stops_count} {sorted(set(transfer_stops))}")
        # print(f"Finish stops: {total_finish_count} {sorted(set(finish_stops))}")

    def verify_on_demand_stops(self):
        print("On demand stops test:")
        # Get list of start stops, end stops and transfer stops
        # Get the list of on demand stops as well
        # If there is any intersection between these two, then print the intersection after sorting it
        # Otherwise print ok
        start_stops, transfer_stops, finish_stops, on_demand_stops = self.get_different_types_of_stops()
        if len(((start_stops | finish_stops | transfer_stops) & on_demand_stops)) == 0:
            print("OK")
        else:
            print(sorted(((start_stops | finish_stops | transfer_stops) & on_demand_stops)))

    def verify_arrival_times(self):
        # print("Arrival time test:")
        arrival_issues_flag = False
        # Get the unique buses first
        buses = set(route.bus_id for route in self.bus_routes)
        # Get all the bus stops for the bus
        for bus in buses:
            stops = [stop for stop in self.bus_routes if stop.bus_id == bus]
            # Now go through each arrival times and check the current one is greater than the previous one
            previous_arrival_time = None
            for stop in stops:
                current_arrival_time = stop.a_time
                if previous_arrival_time is None:
                    previous_arrival_time = current_arrival_time
                    continue
                elif datetime.strptime(previous_arrival_time, "%H:%M") >= datetime.strptime(current_arrival_time,
                                                                                            "%H:%M"):
                    # If not, print bus id and stop name and set a flag
                    arrival_issues_flag = True
                    print(f"bus_id line {bus}: wrong time on station {stop.stop_name}")
                    break
                previous_arrival_time = current_arrival_time
        # Finally, print OK if the flag has not been set
        if not arrival_issues_flag:
            print("OK")

    def print_buses_and_number_of_stops(self):
        buses = defaultdict(int)
        for bus in self.bus_data:
            buses[bus['bus_id']] += 1
        print("Line names and number of stops:")
        for k, v in buses.items():
            print(f"bus_id: {k}, stops: {v}")

    def print_errors(self):
        errors = self.stop_name_errors + \
                 self.stop_type_errors + \
                 self.a_time_errors + \
                 self.bus_id_errors + \
                 self.stop_id_errors + \
                 self.next_stop_errors
        print(f"Type and required field validation: {errors} errors")
        print(f"bus_id: {self.bus_id_errors}")
        print(f"stop_id: {self.stop_id_errors}")
        print(f"stop_name: {self.stop_name_errors}")
        print(f"next_stop: {self.next_stop_errors}")
        print(f"stop_type: {self.stop_type_errors}")
        print(f"a_time: {self.a_time_errors}")

    def validate_bus_id(self, bus):
        try:
            if not isinstance(bus['bus_id'], int):
                self.bus_id_errors += 1
        except TypeError:
            self.bus_id_errors += 1
        except ValueError:
            self.bus_id_errors += 1

    def validate_stop_id(self, bus):
        try:
            if not isinstance(bus['stop_id'], int):
                self.stop_id_errors += 1
        except TypeError:
            self.stop_id_errors += 1
        except ValueError:
            self.stop_id_errors += 1

    def validate_stop_name(self, bus):
        if not isinstance(bus['stop_name'], str):
            self.stop_name_errors += 1
        else:
            # A(?=B)
            pattern = r'[A-Z].+(?=(Road|Avenue|Boulevard|Street)$)'
            if not re.match(pattern, bus['stop_name']):
                self.stop_name_errors += 1
            # else:
            #     print(bus['stop_name'])

    def validate_stop_type(self, bus):
        try:
            if bus['stop_type'] == "":
                return
            if bus['stop_type'] not in "SOF":
                self.stop_type_errors += 1
        except TypeError:
            self.stop_type_errors += 1

    def validate_next_stop(self, bus):
        try:
            if not isinstance(bus['next_stop'], int):
                self.next_stop_errors += 1
        except TypeError:
            self.next_stop_errors += 1
        except ValueError:
            self.next_stop_errors += 1

    def validate_a_time(self, bus):
        try:
            hhmm = bus['a_time']
            hhmm_template = r'\d{2}:\d{2}'
            if not re.match(hhmm_template, hhmm):
                self.a_time_errors += 1
            else:
                split_time = hhmm.split(":")
                if len(split_time) != 2:
                    self.a_time_errors += 1
                else:
                    hh = int(split_time[0])
                    mm = int(split_time[1])
                    if hh > 23:
                        self.a_time_errors += 1
                    if mm > 59:
                        self.a_time_errors += 1
        except TypeError:
            self.a_time_errors += 1
        except AttributeError:
            self.a_time_errors += 1
        except ValueError:
            self.a_time_errors += 1


@dataclass
class EasyRiderBusData:
    bus_id: int
    stop_id: int
    stop_name: str
    next_stop: int
    stop_type: str
    a_time: str


def main():
    easy_bus_rider_company = EasyRiderBusCompany(input())
    easy_bus_rider_company.load_and_verify_database()
    easy_bus_rider_company.verify_print_info_about_routes()
    easy_bus_rider_company.verify_arrival_times()
    easy_bus_rider_company.verify_on_demand_stops()
    # easy_bus_rider_company.print_errors()
    # easy_bus_rider_company.print_buses_and_number_of_stops()


if __name__ == '__main__':
    main()
